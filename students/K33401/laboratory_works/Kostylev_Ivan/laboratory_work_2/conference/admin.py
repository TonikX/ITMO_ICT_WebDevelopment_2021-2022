from django.contrib import admin
from .models import User, Conference, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Conference)
admin.site.register(Review)
