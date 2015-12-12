from django.contrib import admin
from models import Due, Receipt, Project

# Register your models here.


# class DisbursementInline(admin.TabularInline):
#     model = Disbursement
#     extra = 0

# class FundsAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {
#             'fields': ('project_name', 'project_receiver', 'project_cost')}),
#     ]
#     inline = [DisbursementInline]

# admin.site.register(Project, FundsAdmin)
admin.site.register(Due)
admin.site.register(Project)
admin.site.register(Receipt)