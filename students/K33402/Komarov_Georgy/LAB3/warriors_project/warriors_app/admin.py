from django.contrib import admin

from .models import *


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillOfWarrior)
class SkillOfWarriorAdmin(admin.ModelAdmin):
    pass


@admin.register(Warrior)
class WarriorAdmin(admin.ModelAdmin):
    pass
