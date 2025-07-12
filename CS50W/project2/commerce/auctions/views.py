from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django import forms
from decimal import Decimal
from .forms import ListingForm, CommentForm, CategoryForm

from .models import User, Listing, Bid, Watchlist, Comment, Categories

def toggle(item):
    if item:
        return False
    else:
        return True
    
def max_bid(id, user):        
        return Bid.objects.filter(user=user).filter(listing=id).aggregate(Max('bid'))['bid__max']

def index(request):
    listings = Listing.objects.filter(bid_open=True)

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

@login_required(login_url='login')    
def create_listing(request):
    if request.method == 'POST':        
        
        new_listing = ListingForm(request.POST)
        
        if new_listing.is_valid():
           price = new_listing.cleaned_data['price']
           new_listing = new_listing.save(commit=False)
           new_listing.user = request.user
           new_listing.actual_price = price
           new_listing.save() 
            
        return HttpResponseRedirect(reverse("index"))
    else:        
        return render(request, "auctions/create_listings.html", {
            'form': ListingForm
        })
    
@login_required(login_url='login')   
def listing(request, listing_id):
    bid_user = request.user
    listing = Listing.objects.get(id=listing_id)
    my_last_bid = Bid.objects.filter(user=bid_user).filter(listing=listing_id).order_by('-created')[:1]    
    auction_open = listing.user == bid_user and listing.bid_open
    watchlist = Watchlist.objects.get_or_create(user=request.user, listing=listing)
    my_bid = max_bid(listing_id, bid_user) == listing.actual_price
    comments = Comment.objects.filter(listing=listing_id).order_by('-created')
    

    class BidForm(forms.Form) :
        bid = forms.DecimalField(
            label=False,            
            max_digits=8,
            decimal_places=2,
            min_value=listing.actual_price +  Decimal(str(0.01)),
            widget=forms.NumberInput(attrs={'placeholder': "Place a bid"})
            )

    bid_form = BidForm

    

    

    if request.method == 'POST':
        bid = BidForm(request.POST)
        comment = CommentForm(request.POST)    

              
        if 'bid' in request.POST.keys():
                        
            if bid.is_valid():          
                
                new_price = bid.cleaned_data['bid']
                actual_price = listing.actual_price
                bid_user = request.user
                bid_listing = listing
                

                if new_price > actual_price:
                    new_bid = Bid(bid=new_price, listing=bid_listing, user= bid_user)               
                    new_bid.save()
                    listing.actual_price = new_price               
                    listing.save()
        elif 'watchlist' in request.POST.keys():
            
            new_watchlist = Watchlist.objects.get(user=request.user, listing=listing_id)            
            new_watchlist.watchlist=toggle(watchlist[0].watchlist)
            new_watchlist.save()

        elif 'auction' in request.POST.keys():
            listing.bid_open = False
            listing.save()

        elif 'comment' in request.POST.keys():
            if comment.is_valid():
                c = comment.cleaned_data['comment']
                print(c)
                new_comment = Comment(user = request.user, listing = listing, comment = c)
                
                new_comment.save()
                
               
                      

        

        return redirect('listing', listing_id=listing_id)

    
    return render(request, 'auctions/listing.html', {
        'listing' : listing,
        'bid_form': bid_form,
        'comment_form': CommentForm,
        'my_last_bid' : my_last_bid,
        'watchlist' : watchlist[0].watchlist,
        'my_bid': my_bid,
        'comments': comments,
        'auction_open': auction_open
    })

@login_required(login_url='login')
def watchlist(request):
    
    watchlist = Watchlist.objects.filter(user = request.user).filter(watchlist = True) 

    
    
    if request.method == 'POST':        
        drop_watchlist = Watchlist.objects.get(user=request.user, listing=request.POST['id'])            
        drop_watchlist.watchlist=False
        drop_watchlist.save()

    nw = []

    for item in watchlist:
        list_id = item.listing.id
        new_watchlist = {
            'id': item.listing.id,
            'title': item.listing.title,
            'actual_price': item.listing.actual_price,
            'image': item.listing.image,
            'description': item.listing.description,
            'created': item.listing.created,
            'bid_open': item.listing.bid_open,
            'max_bid': max_bid(list_id, request.user)            

        }
        nw.append(new_watchlist)

    return render(request, 'auctions/watchlist.html', {
        'watchlist': nw
    })

@login_required(login_url='login')
def categories(request):
    categories = Categories.objects.all().order_by('category')



    return render(request, 'auctions/categories.html', {
        'categories': categories
    })

def create_categories(request):

    category = CategoryForm(request.POST)

    if request.method == 'POST':
        if category.is_valid():
            new_category = category.cleaned_data['category']
            new_descriptiony = category.cleaned_data['description']
            c = Categories(category=new_category, description=new_descriptiony)
            c.save()
            return HttpResponseRedirect(reverse("categories"))


    return render(request, 'auctions/create_categories.html', {
        'category_form': CategoryForm
    })

def category(request, category):
    category = Categories.objects.get(category=category)
    listings = Listing.objects.filter(category=category, bid_open=True)

    

    return render(request, 'auctions/category.html', {
        'category': category,
        'listings': listings
    })