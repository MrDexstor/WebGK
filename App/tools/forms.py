from django import forms
from Core.models import Label

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', 'qr', 'appName', 'printer']
