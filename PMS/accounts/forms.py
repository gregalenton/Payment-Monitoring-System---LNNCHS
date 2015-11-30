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
    attributes = {
        'name': 'firstname',
        'class': 'form-control',
        'placeholder': 'First Name'
    }

    first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'lastname',
        'class': 'form-control',
        'placeholder': 'Last Name'
    }

    last_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'username',
        'class': 'form-control',
        'placeholder': '20XX12345',
        'rel': 'gp',
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

    password1 = forms.CharField(required=True, min_length=5, widget=forms.TextInput(attrs=attributes))
    password2 = password1

    attributes = {
        'name': 'year',
        'class': 'form-control'
    }

    year_level = forms.IntegerField(widget=forms.Select(attrs=attributes, choices=Student.year_level))

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
        'class': 'form-control',
        'placeholder': 'Andrew...'
    }

    guardian_fn = forms.CharField(max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'glastname',
        'class': 'form-control',
        'placeholder': 'Smith...'
    }

    guardian_ln = forms.CharField(max_length=50, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'gaddress',
        'class': 'form-control',
        'placeholder': '6866 Williams Street Fayetteville, NC 28303'
    }

    guardian_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attributes))

    attributes = {
        'name': 'gcontact',
        'class': 'form-control',
        'placeholder': '441-5656'
    }

    guardian_contact = forms.CharField(max_length=100, widget=forms.TextInput(attrs=attributes))

    attributes = {

    }
    scholarship = forms.ChoiceField(choices=Student.scholarship)
    band_member = forms.BooleanField()

    def save(self, commit=True):
        user = super(AddStudentForm, self).save(commit=commit)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        student = Student()
        student.student_year = self.cleaned_data['year_level']
        student.student_section = self.cleaned_data['section']
        student.student_address = self.cleaned_data['address']
        student.student_guardian_firstname = self.cleaned_data['guardian_fn']
        student.student_guardian_lastname = self.cleaned_data['guardian_ln']
        student.student_guardian_contact = self.cleaned_data['guardian_contact']
        student.student_guardian_address = self.cleaned_data['guardian_address']
        student.student_scholarship = self.cleaned_data['scholarship']
        student.student_bandMem = self.cleande_data['band_member']
        student.student_user = user
        student.save()
