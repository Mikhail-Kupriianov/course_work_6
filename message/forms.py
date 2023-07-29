from django import forms

from main.forms import StyleFormMixin
from message.models import Message


class MessageForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'
        # fields = ('', '', '',)
        # exclude = ('',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message_owner'].widget = forms.HiddenInput()
        self.fields['message_created_at'].widget = forms.HiddenInput()

