from django.contrib import admin
from .models import Student, Admin


class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Account Information', {'fields': ['student_user']}),
        ('Student Info', {'fields': [('student_year', 'student_section'), 'student_address']}),
        ('Guardian Info', {'fields': [('student_guardian_firstname', 'student_guardian_lastname'),
                                      'student_guardian_contact', 'student_guardian_address']}),
        ('Discount Info', {'fields': ['student_scholarship', 'student_sibling', 'student_bandMem']}),
        ('Payment Info', {'fields': ['student_paid', 'student_toPay']})
    )

admin.site.register(Admin)
admin.site.register(Student, StudentAdmin)
