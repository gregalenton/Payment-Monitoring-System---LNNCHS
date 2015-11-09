from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from database.models import Admin, Student


class AdminInline(admin.StackedInline):
    model = Admin
    can_delete = False
    verbose_name_plural = 'admin'


class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'student'


class UserAdmin(admin.ModelAdmin):
    inlines = (AdminInline,)


class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(User, StudentAdmin)


