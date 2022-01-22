from django.contrib import admin
from .models import Company, Flight, Comment

# Register your models here.


admin.site.register(Company)
admin.site.register(Flight)
admin.site.register(Comment)