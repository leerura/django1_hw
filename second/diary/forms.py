from django import forms
from .models import Diary #Diary에 대한 폼을 만들 예정

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title', 'body', 'image'] #모델에서 입력한 애들
        