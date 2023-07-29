from django import forms

from main.forms import StyleFormMixin
from client.models import Client


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = ('', '', '',)
        # exclude = ('',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client_owner'].widget = forms.HiddenInput()
