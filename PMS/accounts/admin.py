from django.contrib import admin
from .models import Student, Admin


class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Account Information', {'fields': ['user']}),
        ('Student Info', {'fields': [('year', 'section'), 'address']}),
        ('Guardian Info', {'fields': [('guardian_firstname', 'guardian_lastname'),
                                      'guardian_contact', 'guardian_address']}),
        ('Discount Info', {'fields': ['scholarship', 'sibling', 'bandMem']}),
        ('Payment Info', {'fields': ['paid', 'toPay']})
    )

admin.site.register(Admin)
admin.site.register(Student, StudentAdmin)
