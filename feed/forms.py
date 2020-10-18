from django import forms
from .models import Image


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'upload_date','likes','comments']
        