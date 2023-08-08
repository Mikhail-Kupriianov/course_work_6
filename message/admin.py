from django.contrib import admin

# Register your models here.
from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'message_title', 'message_content', 'message_created_at', 'message_owner',
    )
    list_filter = ('message_owner',)
    search_fields = ('message_title', 'message_content',)
