from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Specialization)
# admin.site.register(Schedule)
admin.site.register(Doctor)
admin.site.register(ScheduleOfDoctor)
admin.site.register(Cabinet)
admin.site.register(CabinetOfficer)
admin.site.register(ScheduleOfCabinet)
admin.site.register(PriceList)
admin.site.register(Visit)
# admin.site.register(VisitOfPatient)
admin.site.register(MedicalCard)