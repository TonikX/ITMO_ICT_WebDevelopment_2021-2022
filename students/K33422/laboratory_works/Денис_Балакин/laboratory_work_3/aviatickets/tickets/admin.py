from django.contrib import admin

from tickets.models import Airport, Company, Flight

admin.site.register(Company)
admin.site.register(Airport)
admin.site.register(Flight)
