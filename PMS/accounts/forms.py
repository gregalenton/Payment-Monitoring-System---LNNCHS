from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Student


class AdminLoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=5)


class StudentLoginForm(forms.Form):
    username = forms.CharField(min_length=5)
    password = forms.CharField(min_length=5)


class AddStudentForm(forms.ModelForm):
    attributes = {
        'name': 'firstname',
        'class': 'form-control',
    }

    firstname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'lastname',
        'class': 'form-control',
    }

    lastname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'username',
        'class': 'form-control',
        'placeholder': '20XX12345',
        'rel':'gp',
        'data-size': '5',
        'data-character-set': '0-9,u'
    }
    username = forms.CharField(required=True, min_length=5, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'password',
        'class': 'form-control',
        'placeholder': '********',
        'rel': 'gp',
        'data-size': '8',
        'data-character-set': 'a-z,A-Z,0-9'
    }
    password = forms.CharField(required=True, min_length=5, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'year',
        'class': 'form-control'
    }

    year = forms.IntegerField(widget=forms.Select(attrs=attributes, choices=Student.year_level))

    attributes = {
        'name': 'section',
        'class': 'form-control'
    }

    section = forms.CharField(widget=forms.Select(attrs=attributes, choices=Student.section))

    attributes = {
        'name': 'address',
        'class': 'form-control',
        'placeholder': '6866 Williams Street Fayetteville, NC 28303'
    }
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'gfirstname',
        'class': 'form-control'
    }

    gfirstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'glastname',
        'class': 'form-control'
    }

    glastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'gaddress',
        'class': 'form-control',
        'placeholder': '6866 Williams Street Fayetteville, NC 28303'
    }

    gaddress = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'gcontact',
        'class': 'form-control',
        'placeholder': '441-5656'
    }

    gcontact = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'sibling',
        'id': 'yes',
        'value': 'Yes'
    }

    sibling = forms.BooleanField(widget=forms.CheckboxInput(attrs=attributes))

    attributes = {
        'class': 'form-control',
        'name': 'scholarship'
    }

    scholarship = forms.CharField(widget=forms.Select(attrs=attributes, choices=Student.scholarship))

    attributes = {
        'name': 'member',
        'id': 'yes-mem',
        'value': 'Yes'
    }

    band_member = forms.BooleanField(widget=forms.CheckboxInput(attrs=attributes))

