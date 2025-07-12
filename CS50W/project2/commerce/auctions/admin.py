from django.contrib import admin
from .models import *


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created', 'bid_open']

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ['bid', 'listing__title', 'created', 'user']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'listing__title', 'created', 'user']

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['listing__title','watchlist',  'user']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    ...







