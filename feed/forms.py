from django import forms
from .models import Image,Image_Comment


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'upload_date','likes','comments']



class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Image_Comment
		fields = ['comment']

        