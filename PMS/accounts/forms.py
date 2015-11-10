from django import forms
from django.contrib.auth.forms import UserCreationForm


class StudentForm(UserCreationForm):
    username = forms.CharField(
        required=True
    )

    password1 = forms.CharField(
        required=True,
        label=("Password")
    )

    first_name = forms.CharField(
        required=True
    )

    last_name = forms.CharField(
        required=True
    )

    year_level = forms.IntegerField(
        required=True
    )

    section = forms.CharField(
        required=True
    )

    address = forms.CharField(
        required=True
    )


class GuardianForm(forms.ModelForm):
    name = forms.CharField(
        required=True
    )

    address = forms.CharField(
        required=True
    )

    contact = forms.CharField(
        required=True
    )