from django.db import models
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def profile(self):
        profile = Profile.objects.get(user=self)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="user_images", default="default.jpg")

    verified = models.BooleanField(default=False)


class Archive(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Shelf(models.Model):
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    archive = models.ForeignKey(Archive, on_delete=models.DO_NOTHING)
    obs = models.CharField(max_length=100, blank=True)
    boxes = models.IntegerField()

    def update_box_count(self):
        # Count all Box objects related to this shelf
        self.boxes = Box.objects.filter(shelf=self).count()
        self.save()

    def __str__(self):
        return f"{self.id}"


class Box(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.DO_NOTHING)
    obs = models.CharField(max_length=255, blank=True)
    full = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}"


class Situation_type(models.Model):
    type = models.CharField(max_length=100)
    expires_in = models.IntegerField()

    def __str__(self):
        return f"{self.type}"


class Record(models.Model):
    code = models.CharField(max_length=10, unique=True)
    year = models.CharField(max_length=4)
    unity = models.CharField(max_length=4)
    former_code = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def check_digit(self):
        operand = int(f"{self.code}{self.year}816{self.unity}00")
        digit = 98 - operand % 97
        return digit

    def __str__(
        self,
    ):
        return f"{self.code}-{self.check_digit()}.{self.year}.8.16.{self.unity}"


class Archived(models.Model):
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    box = models.ForeignKey(Box, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True)
    volumes = models.IntegerField(default=1)


class Situation(models.Model):
    expire = models.DateField()
    date = models.DateField(auto_now_add=True)
    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    situation_type = models.ForeignKey(Situation_type, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        if self.date is None:
            self.date = timezone.now()
        if self.situation_type.type:
            self.expire = self.date + relativedelta(
                years=self.situation_type.expires_in
            )
        super(Situation, self).save(*args, **kwargs)


class Person(models.Model):
    name = models.CharField(max_length=100)


class Par(models.Model):

    PAR_TYPE = [
        ("d", "Defendant"),
        ("p", "Plaintiff"),
    ]

    record = models.ForeignKey(Record, on_delete=models.DO_NOTHING)
    par = models.ForeignKey(Person, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=12, choices=PAR_TYPE)


from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Box)
@receiver(post_delete, sender=Box)
def update_shelf_box_count(sender, instance, **kwargs):
    if instance.shelf:
        instance.shelf.update_box_count()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
