from .models import User, Listing, Bid, Watchlist, Comment, Categories
from django.forms import modelform_factory
from django import forms
from decimal import Decimal



ListingForm = modelform_factory(Listing, fields=['title', 'description', 'price', 'image', 'category'])

CategoryForm = modelform_factory(Categories, exclude=[])


class CommentForm(forms.Form) :
        comment = forms.CharField(
            label=False,            
            widget=forms.TextInput(attrs={'placeholder': "Place a comment"})
            )
        

