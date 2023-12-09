from django import forms
from dj_form.models import ModelForm


class Form2(forms.ModelForm):
    class Meta:
        model = ModelForm
        fields = '__all__'