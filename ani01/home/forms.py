from django import forms
from .models import *

class Question_form(forms.ModelForm):
    class Meta:
        model=question
        fields= ['author','question']

class Answer_form(forms.ModelForm):
    class Meta:
        model=answer
        fields= ['author','question','answer']

class Comment_form(forms.ModelForm):
    class Meta:
        model=comment
        fields= ['author','question','comment']
        
        