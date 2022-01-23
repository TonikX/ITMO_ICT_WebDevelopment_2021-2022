from django.contrib.auth.models import Group
from django.contrib import admin

# Remove group model from admin site
admin.site.unregister(Group)
