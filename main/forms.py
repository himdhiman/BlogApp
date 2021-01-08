from django import forms
from main import models

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

