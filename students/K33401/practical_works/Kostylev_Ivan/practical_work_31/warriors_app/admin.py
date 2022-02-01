from django.contrib import admin

from warriors_app.models import Warrior, Skill, SkillOfWarrior, Profession

admin.site.register(Warrior)
admin.site.register(Skill)
admin.site.register(SkillOfWarrior)
admin.site.register(Profession)
