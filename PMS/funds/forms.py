from django import forms
from .models import Due, Project, Receipt


class AddFundsForm(forms.ModelForm):
    attributes = {
        'placeholder': 'Library Fee',
        'class': 'form-control required',
    }

    fundname = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'placeholder': '500',
        'class': 'form-control required',
    }

    cost = forms.FloatField(required=True, widget=forms.TextInput(attrs=attributes))

    class Meta:
        model = Due
        fields = ['fundname', 'cost']

    def save(self, commit=True):
        due = Due()
        due.name = self.cleaned_data['fundname']
        due.cost = self.cleaned_data['cost']
        due.save()


class AddProjectForm(forms.ModelForm):
    attributes = {
        'placeholder': 'Library PCs',
        'class': 'form-control required',
    }

    fundname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'placeholder': '500',
        'class': 'form-control required',
    }

    cost = forms.FloatField(required=True, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'placeholder': '500',
        'class': 'form-control required',
    }

    receiver = forms.CharField(required=True, max_length=50,  widget=forms.TextInput(attrs=attributes))

    class Meta:
        model = Project
        fields = ['fundname', 'receiver', 'cost']

    def save(self, commit=True):
        project = Project()
        project.name = self.cleaned_data['fundname']
        project.cost = self.cleaned_data['cost']
        project.receiver = self.cleaned_data['receiver']
        project.save()


class AddPaymentForm(forms.ModelForm):

    attributes = {
        'class': 'form-control required',
    }

    student_id = forms.CharField(required=True, max_length=50,  widget=forms.Select(attrs=attributes))
    
    attributes = {
        'placeholder': '500',
        'class': 'form-control required',
    }

    cost = forms.FloatField(required=True, widget=forms.TextInput(attrs=attributes))
    
    class Meta:
        model = Receipt
        fields = ['student_id', 'cost']

    def save(self, commit=True):
        receipt = Receipt()
        receipt.student_id = self.cleaned_data['student_id']
        receipt.payment = self.cleaned_data['cost']
        receipt.save()

