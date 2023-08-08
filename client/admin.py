from django.contrib import admin

# Register your models here. изменить
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'client_second_name', 'client_first_name', 'client_surname',
        'client_email', 'client_comments', 'client_owner',
    )
    list_filter = ('client_owner',)
    search_fields = ('client_second_name', 'client_comments',)





