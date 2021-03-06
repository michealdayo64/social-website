from django.contrib import admin
from .models import UserProfileInfo, Contact


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'profile_pic']


admin.site.register(UserProfileInfo, ProfileAdmin)
admin.site.register(Contact)