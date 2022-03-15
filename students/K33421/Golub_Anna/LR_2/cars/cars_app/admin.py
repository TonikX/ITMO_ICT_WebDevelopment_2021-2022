from django.contrib import admin

from .models import User, Car, Ownership, License
# from .models import Car, Ownership, License

from django.contrib.auth import get_user_model

# Owner = get_user_model()

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Ownership)
admin.site.register(License)
