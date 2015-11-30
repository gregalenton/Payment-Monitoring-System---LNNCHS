from django.contrib import admin
from .models import Due, Disbursement, Project, Receipt


class DisbursementInline(admin.TabularInline):
    model = Disbursement
    extra = 0


class FundsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('project_name', 'project_receiver', 'project_cost')}),
    ]
    inline = [DisbursementInline]

admin.site.register(Project, FundsAdmin)
