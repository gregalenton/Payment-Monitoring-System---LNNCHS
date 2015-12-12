from django import forms
from . import models



class AddFundsForm(forms.ModelForm):
    class Meta:
        model = models.Due
        fields = ['due_name', 'due_cost']


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['project_name', 'project_receiver', 'project_cost']
