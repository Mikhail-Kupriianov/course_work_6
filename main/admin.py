from django.contrib import admin

from main.models import Distribution


@admin.register(Distribution)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'distribution_name', 'distribution_start', 'distribution_end',
        'distribution_is_active', 'periodicity', 'status', 'distribution_owner',
    )
    list_filter = ('distribution_is_active', 'periodicity', 'status',)
    search_fields = ('distribution_name', 'status',)






