from django.contrib import admin
from .models import Warrior, Profession, Skill, SkillOfWarrior

class Warrior_Admin(admin.ModelAdmin):
    pass

class Profession_Admin(admin.ModelAdmin):
    pass

class Skill_Admin(admin.ModelAdmin):
    pass

class SkillOfWarrior_Admin(admin.ModelAdmin):
    pass

admin.site.register(Warrior, Warrior_Admin)
admin.site.register(Profession, Profession_Admin)
admin.site.register(Skill, Skill_Admin)
admin.site.register(SkillOfWarrior, SkillOfWarrior_Admin)