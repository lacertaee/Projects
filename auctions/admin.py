from django.contrib import admin
from .models import Listing, Watchlist, User, Category, Bids, Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(Category)
admin.site.register(Bids)
admin.site.register(Comments)