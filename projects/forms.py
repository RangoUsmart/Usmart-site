from django import forms
from django.forms import Textarea
# from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'label':"daca", 'size': 100, "class":"form-control"}),
            'description': forms.TextInput(attrs={'size': 100, "class":"form-control"}),
            'content': forms.TextInput(attrs={'size': 8000, "class":"form-control"}),

        }
        # labels = {
        #     'title': ('title'),
        # }