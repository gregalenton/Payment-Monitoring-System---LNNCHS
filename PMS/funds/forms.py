from django import forms
from . import models



class AddFundsForm(forms.ModelForm):
    class Meta:
        model = models.Due
        fields = ['due_name', 'due_cost']

	def save(self, commit=True):
		fund = super(AddFundsForm, self).save(commit=commit)
		fund.due_cost = self.cleaned_data['due_cost']
		fund.save()


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['project_name', 'project_receiver', 'project_cost']
