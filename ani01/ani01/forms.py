from django import forms
from home1.models import userupload

class studentforms(forms.ModelForm):
    class Meta():
        model=userupload
        fields="__all__"