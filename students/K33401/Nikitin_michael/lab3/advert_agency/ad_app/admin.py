from django.contrib import admin

from .models import *

admin.site.register(Client)
admin.site.register(Worker)
admin.site.register(Service)
admin.site.register(Application)
admin.site.register(Assignment)