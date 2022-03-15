from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Readers)
admin.site.register(Halls)
admin.site.register(BookAttachment)
admin.site.register(ReaderAttachment)
