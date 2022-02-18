from django.contrib import admin
from .models import Users, Racers, Race, RaceRacers, Comments

admin.site.register(Users)
admin.site.register(Racers)
admin.site.register(Race)
admin.site.register(RaceRacers)
admin.site.register(Comments)
