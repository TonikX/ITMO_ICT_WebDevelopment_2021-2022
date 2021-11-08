from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Listing)
admin.site.register(ListingComment)
admin.site.register(Bid)
admin.site.register(WatchList)
admin.site.register(ListingCategory)
