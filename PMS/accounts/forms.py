from django import forms
from models import *
from django.contrib.auth.models import User


class AddUserForm(forms.ModelForm):
    attribute = {
        'placeholder': 'placeholder'
    }
    attribute['placeholder'] = 'Last Name'
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attribute['placeholder'] = 'First Name'
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attribute['placeholder'] = 'Middle Name'
    middle_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attribute = {
        'type': 'date',
        'placeholder': 'Birthday',
    }

    birthday = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs=attribute
        )
    )

    attribute['placeholder'] = 'Gender'
    gender = forms.CharField(
        required=True,
        widget=forms.Select(
            attrs=attribute,
            choices=GENDER
        )
    )

    def save(self, commit=True):
        student = super(AddStudentForm, self).save(commit=commit)
        student.lastname = self.cleaned_data['last_name']
        student.firstname = self.cleaned_data['first_name']
        student.middlename = self.cleaned_data['middle_name']
        student.birthday = self.cleaned_data['birthday']
        student.gender = self.cleaned_data['gender']
        student.save()

    class Meta:
        model = StudentInfo
        fields = ('first_name', 'last_name', 'middlename', 'birthday', 'gender')