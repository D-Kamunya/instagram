from django import forms
from .models import Image,Image_Comment


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'upload_date','likes','comments']



class NewCommentForm(forms.ModelForm):
    comment = forms.CharField(label=False, widget=forms.TextInput(attrs={"class":"form-control comment",
                                                                         "placeholder":"Add a comment..."}))
    class Meta:
        model=Image_Comment
        fields=("comment",)



        