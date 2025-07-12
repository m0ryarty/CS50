from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now=True)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Bid(models.Model):
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    actual_price = models.DecimalField(max_digits=8, decimal_places=2)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    