from django import forms
from models import StudentInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['lastname', 'firstname', 'middlename', 'birthday', 'gender']
        # attribute = {
        #     'placeholder': 'placeholder'
        # }
        # attribute['placeholder'] = 'Last Name'
        # lastname = forms.CharField(
        #     required=True,
        #     widget=forms.TextInput(attrs=attribute)
        # )

        # attribute['placeholder'] = 'First Name'
        # firstname = forms.CharField(
        #     required=True,
        #     widget=forms.TextInput(attrs=attribute)
        # )

        # attribute['placeholder'] = 'Middle Name'
        # middlename = forms.CharField(
        #     required=True,
        #     widget=forms.TextInput(attrs=attribute)
        # )

        # attribute = {
        #     'type': 'date',
        #     'placeholder': 'Birthday',
        # }

        # birthday = forms.DateField(
        #     required=True,
        #     widget=forms.DateInput(
        #         attrs=attribute
        #     )
        # )

        # attribute['placeholder'] = 'Gender'
        # gender = forms.CharField(
        #     required=True,
        #     widget=forms.Select(
        #         attrs=attribute,
        #         choices=StudentInfo.GENDER
        #     )
        # )



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
