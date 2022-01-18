from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Warrior)
admin.site.register(Profession)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)