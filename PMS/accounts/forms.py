from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Student


class AdminLoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=5)


class StudentLoginForm(forms.Form):
    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=5)


class AddStudentForm(UserCreationForm):
    first_name = forms.CharField(required=True, max_length=50)
    last_name = forms.CharField(required=True, max_length=50)
    username = forms.CharField(required=True, min_length=5)
    password = forms.CharField(required=True, min_length=5)
    year_level = forms.ChoiceField(choices=Student.year_level)
    section = forms.ChoiceField(choices=Student.section)
    address = forms.CharField(max_length=100)
    guardian_fn = forms.CharField(max_length=50)
    guardian_ln = forms.CharField(max_length=50)
    guardian_contact = forms.CharField(max_length=100)
    guardian_address = forms.CharField(max_length=100)
    scholarship = forms.ChoiceField(choices=Student.scholarship)
    band_member = forms.BooleanField()

    def save(self, commit=True):
        user = super(AddStudentForm, self).save(commit=commit)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password']
        user.