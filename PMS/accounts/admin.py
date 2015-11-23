from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = StudentInfo
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(StudentInfo)