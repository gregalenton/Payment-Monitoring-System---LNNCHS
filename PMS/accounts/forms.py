from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from database.models import Admin, Student


class AddStudentForm(UserCreationForm):
    attribute = {
        'class': 'username',
        'placeholder': 'username',
    }

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attribute = {
        'class': 'password',
        'placeholder': 'password',
    }

    password1 = forms.CharField(
        required=True,
        label=_("Password"),
        widget=forms.PasswordInput(attrs=attribute)
    )

    attribute = {
        'class': 'fname',
        'placeholder': 'first name',
    }

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    attribute = {
        'class': 'form-control',
        'id': 'yearlevel',
    }

    year_level = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs=attribute,
            choices=Student.year_level
        )
    )

    attribute = {
        'class': 'form-control',
        'id': 'section',
    }

    section = forms.ChoiceField(
        required=True,
        widget=forms.Select(
            attrs=attribute,
            choices=Student.section
        )
    )

    attribute = {
        'class': 'address',
        'placeholder': 'address',
    }

    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=attribute)
    )

    def save(self, commit=True):
        user = super(AddStudentForm, self).save(commit=commit)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        profile = Student()
        profile.student_year = self.cleaned_data['year_level']
        profile.student_section = self.cleaned_data['section']
        profile.user = user
        profile.save()