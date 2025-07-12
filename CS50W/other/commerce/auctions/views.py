from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid
from django.forms import modelform_factory

Listing_form = modelform_factory(Listing, exclude = ['created'])
Bid_form = modelform_factory(Bid, fields=['bid'])


def index(request):
    listings = Listing.objects.all()

    return render(request, "auctions/index.html", {
        'listings': listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def new_listing(request):
    if request.method == "POST":        
        listing = Listing_form(request.POST)
        if listing.is_valid():

            listing.save()
            return HttpResponseRedirect(reverse("index"))
    else:        
        return render(request, "auctions/create_listings.html", {
            'form': Listing_form
        })
    
def listing(request, listing_id):
    
    listing = Listing.objects.get(id=listing_id)
    return render(request, 'auctions/listing.html', {
        'listing' : listing,
        'bid_form': Bid_form
    })
