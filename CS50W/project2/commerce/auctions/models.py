from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Categories(models.Model):
    category = models.CharField(unique=True, max_length=255)
    description = models.TextField(max_length=255)
    
    def __str__(self):
        return f'{self.category}'
    
class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    actual_price = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now=True)
    image = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_open = models.BooleanField(default=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title: {self.title}, Description: {self.description}, Price: {self.price}, Actual Price:"{self.actual_price}, Created: {self.created}, Image: {self.image}, Open: {self.bid_open}'

class Bid(models.Model):
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.bid} created at {self.created}'

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.comment}'
    
class Watchlist(models.Model):
    watchlist = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.listing.title} is {self.watchlist} for {self.user}'
    