from django import forms
from basic.models import number
class ino(forms.ModelForm):
    class Meta:
        model = number
        fields = ['no']