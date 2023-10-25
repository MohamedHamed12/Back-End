from django.contrib import admin

from accounts.models import PhoneModel, Profile

# Register your models here.
admin.site.register(PhoneModel)
admin.site.register(Profile)