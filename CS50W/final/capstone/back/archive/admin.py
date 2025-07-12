from django.contrib import admin
from archive.models import (
    Situation_type,
    User,
    Profile,
    Archive,
    Shelf,
    Box,
    Record,
    Situation,
    Person,
    Par,
)


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email"]


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ["verified"]
    list_display = ["user", "full_name", "verified"]


class Situation_typeAdmin(admin.ModelAdmin):
    list_display = [
        "type",
        "expires_in",
    ]


class ArchiveAdmin(admin.ModelAdmin):
    list_display = ["name", "address"]


class ShelfAdmin(admin.ModelAdmin):
    list_display = ["type", "location", "capacity", "archive", "obs"]


class BoxAdmin(admin.ModelAdmin):
    list_display = ["shelf", "obs"]


class RecordAdmin(admin.ModelAdmin):
    list_display = ["code", "year", "unity"]


class SituationAdmin(admin.ModelAdmin):
    list_display = ["record", "situation_type", "date", "expire"]


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name"]


class ParAdmin(admin.ModelAdmin):
    list_display = ["record", "par", "type"]


admin.site.register(Person, PersonAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Situation_type, Situation_typeAdmin)
admin.site.register(Archive, ArchiveAdmin)
admin.site.register(Shelf, ShelfAdmin)
admin.site.register(Box, BoxAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(Situation, SituationAdmin)
admin.site.register(Par, ParAdmin)
