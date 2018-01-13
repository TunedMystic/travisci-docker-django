from django.contrib import admin

from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    readonly_fields = ('id',)
    search_fields = ('name', 'id')
    exclude = ('updated_on',)


admin.site.register(Company, CompanyAdmin)
