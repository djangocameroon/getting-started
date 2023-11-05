from django import forms
from .models import Toast

class ToastForm(forms.ModelForm):
    class Meta:
        model = Toast
        fields = ['name', 'email',]