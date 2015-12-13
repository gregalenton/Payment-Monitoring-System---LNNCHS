from django.contrib import admin
from .models import Due, Disbursement, Project, Receipt


class DisbursementInline(admin.TabularInline):
    model = Disbursement
    extra = 0


class FundsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('name', 'receiver', 'cost')}),
    ]
    inline = [DisbursementInline]

admin.site.register(Project, FundsAdmin)
admin.site.register(Due)