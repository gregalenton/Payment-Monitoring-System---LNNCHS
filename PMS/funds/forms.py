from django import forms
from . import models


class AddFundsForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['project_name', 'project_receiver', 'project_cost']


