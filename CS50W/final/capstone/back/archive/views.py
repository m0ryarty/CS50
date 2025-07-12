import re

import json
from archive.models import (
    User,
    Box,
    Shelf,
    Archive,
    Record,
    Archived,
    Situation,
    Situation_type,
    Person,
    Par,
)

from archive.serializer import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
)

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework import serializers
from archive.utils import (
    archive_summary,
    box_all_volumes,
    box_volumes,
    record_volumes,
    spare_boxes,
    spare_shelves,
    archives,
    record_situation,
    situations_type,
)


def response_data():
    archives_data = json.loads(archives())
    archive_summary_data = json.loads(archive_summary())
    box_all_volumes_data = json.loads(box_all_volumes())
    box_volumes_data = json.loads(box_volumes())
    record_volumes_data = json.loads(record_volumes())
    boxes_data = json.loads(spare_boxes())
    shelves_data = json.loads(spare_shelves())
    situation_data = json.loads(record_situation())
    situations_data = json.loads(situations_type())

    data = {
        "boxes": boxes_data,
        "shelves": shelves_data,
        "archives": archives_data,
        "box_volumes": box_volumes_data,
        "record_volumes": record_volumes_data,
        "box_all_vols": box_all_volumes_data,
        "summary": archive_summary_data,
        "situation": situation_data,
        "situations": situations_data,
    }
    return data


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_situations(request):
    data = json.loads(request.body)
    record = Record.objects.get(id=data["id"])
    situation = Situation_type.objects.get(id=data["situation"])

    new_situation = Situation(record=record, situation_type=situation)

    new_situation.save()

    return Response({"response": response_data()}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_archive(request):
    data = json.loads(request.body)
    new_archive = Archive(
        name=data["name"],
        address=data["address"],
    )
    new_archive.save()

    return Response({"response": response_data()}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def exist_record(request):
    if request.method == "POST":

        data = json.loads(request.body)

        splitted = re.split(r"[-.]", data["record"])

        code = splitted[0]
        year = splitted[2]
        unity = splitted[5]

        record = Record.objects.filter(
            code=code,
            year=year,
            unity=unity,
        )

        if record:
            return Response(
                {"exists": True, "record": record[0].id}, status=status.HTTP_200_OK
            )
        else:
            return Response({"exists": False}, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def archiving(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            splitted = re.split(r"[-.]", data["number"])

            code = splitted[0]
            year = splitted[2]
            unity = splitted[5]

            volumes = data["volumes"]
            box = Box.objects.get(id=data["box"])
            user = User.objects.get(id=request.user.id)

            record = Record.objects.filter(
                code=code,
                year=year,
                unity=unity,
            )

            if data.get("full"):
                box.full = True
                box.save()

            if not record:

                former_code = data["former_code"]

                new_record = Record(
                    code=code,
                    year=year,
                    unity=unity,
                    former_code=former_code,
                    user=user,
                )
                new_record.save()

                plaintiff = data["plaintiff"]
                defendant = data["defendant"]

                exist_plaintiff = Person.objects.filter(name=plaintiff)
                exist_defendant = Person.objects.filter(name=defendant)

                if not exist_plaintiff:
                    new_plaintiff = Person(name=plaintiff)
                    new_plaintiff.save()

                if not exist_defendant:
                    new_defendant = Person(name=defendant)
                    new_defendant.save()

                existing_record = Record.objects.filter(
                    code=code,
                    year=year,
                    unity=unity,
                )
                saving_record = Record.objects.get(id=existing_record[0].id)

                record_plaintiff = Person.objects.get(name=plaintiff)
                record_defendant = Person.objects.get(name=defendant)

                saving_plaintiff = Par(
                    record=saving_record, par=record_plaintiff, type="p"
                )

                saving_defendant = Par(
                    record=saving_record, par=record_defendant, type="d"
                )
                new_situation = Situation(
                    record=saving_record,
                    situation_type=Situation_type.objects.get(id=1),
                )
                new_situation.save()

                saving_defendant.save()
                saving_plaintiff.save()

        except Exception as e:
            print(str(e))
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        existing_record = Record.objects.filter(
            code=code,
            year=year,
            unity=unity,
        )
        saving_record = Record.objects.get(id=existing_record[0].id)

        new_archived = Archived(
            record=saving_record, box=box, user=user, volumes=volumes
        )
        new_archived.save()

    return Response({"response": response_data()}, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def boxes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        shelf = Shelf.objects.filter(id=data["shelf"])[0]
        new_box = Box(shelf=shelf, obs=data["Obs"])
        new_box.save()

    elif request.method == "PUT":
        data = json.loads(request.body)
        box = Box.objects.get(id=data["id"])
        shelf = Shelf.objects.filter(id=data["shelf"])[0]
        box.shelf = shelf
        box.obs = data["obs"]
        box.full = data["full"]

        box.save()

    return Response({"response": response_data()}, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "PUT"])
@permission_classes([IsAuthenticated])
def shelves(request):
    if request.method == "POST":
        data = json.loads(request.body)
        archive = Archive.objects.get(id=data["archive"])
        new_shelf = Shelf(
            archive=archive,
            boxes=0,
            capacity=data["capacity"],
            location=data["location"],
            type=data["type"],
        )
        new_shelf.save()

    elif request.method == "PUT":
        data = json.loads(request.body)

        shelf = Shelf.objects.get(id=data["id"])
        archive = Archive.objects.get(id=data["archive"])

        shelf.archive = archive
        shelf.capacity = data["capacity"]
        shelf.location = data["location"]
        shelf.type = data["type"]
        shelf.obs = data["obs"]

        shelf.save()

    return Response({"response": response_data()}, status=status.HTTP_200_OK)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getRoutes(request):
    routes = ["/archive/token/", "/register/", "/archive/token/refresh/", "/", "/boxes"]

    return Response(routes)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == "GET":
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({"response": data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        text = "Hello buddy"
        data = (
            f"Congratulation your API just responded to POST request with text: {text}"
        )
        return Response({"response": data}, status=status.HTTP_200_OK)

    return Response({}, status.HTTP_400_BAD_REQUEST)
