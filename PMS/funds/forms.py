from django import forms
from . import models


class AddFundsForm(forms.ModelForm):
    class Meta:
        model = models.Due
        fields = ['name', 'cost']

class AddProjectForm(forms.ModelForm):
	class Meta:
		model = models.Project
		fields = [
			'name',
			'receiver',
			'cost'
		]

class AddPaymentForm(forms.ModelForm):
	class Meta:
		model = models.Payment
		fields = ['name']