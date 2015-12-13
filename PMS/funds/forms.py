from django import forms
from . import models


class AddFundsForm(forms.ModelForm):
    class Meta:
        model = models.Due
        fields = ['name', 'cost']