from django import forms
from .models import Diary

class BlogForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'writer', 'body', 'image']
        