from django import forms
from django.forms import Textarea
# from ckeditor.widgets import CKEditorWidget
from .models import MainUserInfo

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = MainUserInfo
        fields = ['user_subscribe',]
        widgets = {
            'user_subscribe': forms.TextInput(attrs={'size': 8000, "class":"form-control"}),

        }
        # labels = {
        #     'title': ('title'),
        # }