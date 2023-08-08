from django import forms

from main.models import Distribution, CDCross


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name is not 'distribution_is_active':
                field.widget.attrs['class'] = 'form-control'


class DistributionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Distribution
        fields = '__all__'
        # fields = ('', '', '',)
        # exclude = ('',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['distribution_owner'].widget = forms.HiddenInput()


class CDCrossForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = CDCross
        fields = '__all__'
