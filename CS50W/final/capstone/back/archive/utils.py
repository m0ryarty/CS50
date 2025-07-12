from datetime import datetime
import numpy as np
from rest_framework.views import exception_handler
import pandas as pd

from archive.models import (
    Box,
    Shelf,
    Archived,
    Situation,
    Situation_type,
    Archive,
    Record,
)

pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.max_columns", None)  # Show all column names


def get_situations_type():
    situations_type_df = pd.DataFrame.from_records(
        list(Situation_type.objects.values_list("id", "type", "expires_in")),
        columns=["id", "type", "expires_in"],
    )
    return situations_type_df


def get_all_data():

    archives_df = pd.DataFrame.from_records(
        list(Archive.objects.values_list("id", "name", "address")),
        columns=["id", "name", "address"],
    )

    boxes_df = pd.DataFrame.from_records(
        list(Box.objects.values_list("id", "shelf", "full", "obs")),
        columns=["id", "shelf", "full", "obs"],
    ).rename(columns={"obs": "box_obs"})

    shelves_df = pd.DataFrame.from_records(
        list(
            Shelf.objects.values_list(
                "id", "archive", "type", "location", "capacity", "boxes", "obs"
            )
        ),
        columns=["id", "archive", "type", "location", "capacity", "boxes", "obs"],
    ).rename(columns={"obs": "shelf_obs", "type": "shelf_type"})

    archived_data_df = pd.DataFrame.from_records(
        list(Archived.objects.values_list("id", "record", "box", "volumes")),
        columns=["id", "record", "box", "volumes"],
    )

    situations_df = pd.DataFrame.from_records(
        list(
            Situation.objects.values_list(
                "id", "expire", "date", "record", "situation_type"
            )
        ),
        columns=["id", "expire", "date", "record", "situation_type"],
    )

    situations_type_df = get_situations_type()

    # Creating a dataframe with all needed data
    # Merge situations_df with situations_type_df

    all_data_df = (
        pd.merge(archives_df, shelves_df, left_on="id", right_on="archive", how="left")
        .rename(columns={"id_x": "id_archives", "id_y": "id_shelves"})
        .drop(columns=["address", "id_archives", "shelf_type", "location", "shelf_obs"])
    )

    all_data_df = (
        pd.merge(
            all_data_df,
            boxes_df,
            left_on="id_shelves",
            right_on="shelf",
            how="left",
        )
        .rename(columns={"id": "id_boxes"})
        .drop(columns=["full", "id_shelves", "box_obs"])
    )

    all_data_df = (
        pd.merge(
            all_data_df,
            archived_data_df,
            left_on="id_boxes",
            right_on="box",
            how="left",
        )
        .drop(columns=["id", "box"])
        .fillna(0)
    )

    for col in all_data_df.select_dtypes(include=["float"]).columns:
        all_data_df[col] = all_data_df[col].astype(int)

    all_data_df = (
        pd.merge(
            all_data_df,
            situations_df.drop_duplicates(subset="record"),
            left_on="record",
            right_on="record",
            how="left",
        )
        .drop(columns=["id"])
        .fillna(0)
    )

    for col in all_data_df.select_dtypes(include=["float"]).columns:
        all_data_df[col] = all_data_df[col].astype(int)

    all_data_df = (
        pd.merge(
            all_data_df,
            situations_type_df,
            left_on="situation_type",
            right_on="id",
            how="left",
        )
        .drop(columns=["id", "situation_type"])
        .fillna(0)
    )

    for col in all_data_df.select_dtypes(include=["float"]).columns:
        all_data_df[col] = all_data_df[col].astype(int)

    return all_data_df


def get_summary():
    all_data_df = get_all_data()
    situations_df = situations().drop(
        columns=["code", "year", "unity", "digit", "expire", "date"]
    )
    situations_type_df = get_situations_type()

    situations_df["expired"] = situations_df["days_to_expire"] <= 0

    situations_df = pd.merge(
        situations_df,
        situations_type_df,
        left_on="situation_type",
        right_on="id",
        how="left",
    )

    c_situations_df = (
        situations_df.groupby(["archive", "type"])
        .size()
        .reset_index(name="count")
        .pivot(index="archive", columns="type", values="count")
        .reset_index()
    ).fillna(0)

    for col in c_situations_df.select_dtypes(include=["float"]).columns:
        c_situations_df[col] = c_situations_df[col].astype(int)

    expired_counts = situations_df.groupby("archive").agg(expired=("expired", "sum"))

    situations_summary_df = pd.merge(
        c_situations_df,
        expired_counts,
        left_on="archive",
        right_on="archive",
        how="left",
    )

    summary_df = (
        all_data_df.groupby(["archive"])
        .agg(
            num_boxes=("id_boxes", "nunique"),
            num_shelves=("shelf", "nunique"),
            total_volumes=("volumes", "sum"),
        )
        .reset_index()
    )

    summary_df = pd.merge(
        summary_df,
        situations_summary_df,
        left_on="archive",
        right_on="archive",
        how="left",
    )

    return summary_df


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data["status_code"] = response.status_code

    return response


def record_volumes():

    archived_data_df = pd.DataFrame.from_records(
        list(Archived.objects.values_list("id", "record", "box", "volumes")),
        columns=["id", "record", "box", "volumes"],
    )

    record_volumes = (
        archived_data_df.groupby("record")["volumes"].sum().reset_index()
    ).to_json(orient="records", lines=False)
    return record_volumes


def box_volumes():
    archived_data_df = pd.DataFrame.from_records(
        list(Archived.objects.values_list("id", "record", "box", "volumes")),
        columns=["id", "record", "box", "volumes"],
    )

    box_volumes_df = (
        archived_data_df.groupby(["record", "box"])["volumes"].sum().reset_index()
    )

    return box_volumes_df.to_json(orient="records", lines=False)


def box_all_volumes():

    archived_data_df = pd.DataFrame.from_records(
        list(Archived.objects.values_list("id", "record", "box", "volumes")),
        columns=["id", "record", "box", "volumes"],
    )

    box_all_volumes = (
        archived_data_df.groupby("box")
        .agg(total_volumes=("volumes", "sum"))
        .reset_index()
    )

    return box_all_volumes.to_json(orient="records", lines=False)


def archive_summary():

    summary_df = get_summary()

    return summary_df.to_json(orient="records", lines=False)


def spare_boxes():
    boxes_df = pd.DataFrame.from_records(
        list(Box.objects.values_list("id", "shelf", "full", "obs")),
        columns=["id", "shelf", "full", "obs"],
    ).rename(columns={"obs": "box_obs"})

    only_spare_boxes = boxes_df[boxes_df["full"] == False]

    return only_spare_boxes.to_json(orient="records", lines=False)


def spare_shelves():

    shelves_df = pd.DataFrame.from_records(
        list(
            Shelf.objects.values_list(
                "id", "archive", "type", "location", "capacity", "boxes", "obs"
            )
        ),
        columns=["id", "archive", "type", "location", "capacity", "boxes", "obs"],
    )

    only_spare_shelves = shelves_df[shelves_df["capacity"] > shelves_df["boxes"]]

    return only_spare_shelves.to_json(orient="records", lines=False)


def archives():
    archives_df = pd.DataFrame.from_records(
        list(Archive.objects.values_list("id", "name", "address")),
        columns=["id", "name", "address"],
    ).to_json(orient="records", lines=False)

    return archives_df


def situations():

    all_data_df = get_all_data()

    archive_record_df = all_data_df[["archive", "record"]]

    archive_record_df = archive_record_df.drop_duplicates(subset="record")

    situations_df = pd.DataFrame.from_records(
        list(
            Situation.objects.values_list(
                "id", "expire", "date", "record", "situation_type"
            )
        ),
        columns=["id", "expire", "date", "record", "situation_type"],
    )

    record_df = pd.DataFrame.from_records(
        list(
            Record.objects.values_list(
                "id", "code", "year", "unity", "former_code", "user"
            )
        ),
        columns=["id", "code", "year", "unity", "former_code", "user"],
    )

    record_situation_df = pd.merge(
        situations_df, record_df, left_on="record", right_on="id", how="left"
    ).drop(columns=["id_x", "id_y", "former_code", "user"])

    record_situation_df = pd.merge(
        record_situation_df,
        archive_record_df,
        left_on="record",
        right_on="record",
        how="left",
    )

    record_situation_df["expire"] = pd.to_datetime(record_situation_df["expire"])

    today = datetime.now()

    # Calculate the number of days from now to the expire date
    record_situation_df["days_to_expire"] = (
        record_situation_df["expire"] - today
    ).dt.days

    def digit():
        r1 = record_situation_df["code"].astype(int) % 97
        r2 = (r1.astype(str) + record_situation_df["year"] + "816").astype(int) % 97
        r3 = (r2.astype(str) + record_situation_df["unity"] + "00").astype(int) % 97
        result = 98 - r3

        return result

    record_situation_df["digit"] = digit()

    record_situation_df = record_situation_df.sort_index(ascending=False)

    record_situation_df = record_situation_df.drop_duplicates(subset=["record"])

    return record_situation_df


def record_situation():
    all_situations = situations()
    return all_situations.to_json(orient="records", lines=False)


def situations_type():
    situation_types_df = pd.DataFrame.from_records(
        list(Situation_type.objects.values_list("id", "type")),
        columns=["id", "type"],
    ).to_json(orient="records", lines=False)

    return situation_types_df
