from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Student


class AdminLoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)


class StudentLoginForm(forms.Form):
    username = forms.CharField(min_length=5)
    password = forms.CharField(widget=forms.PasswordInput, min_length=5)


class AddStudentForm(UserCreationForm):
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

    year = forms.IntegerField(widget=forms.Select(attrs=attributes, choices=Student.YEAR_LEVELS))

    attributes = {
        'name': 'section',
        'class': 'form-control'
    }

    section = forms.CharField(widget=forms.Select(attrs=attributes, choices=Student.SECTION_CHOICE))

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

    scholarship = forms.CharField(widget=forms.Select(attrs=attributes, choices=Student.SCHOLARSHIP_CHOICES))

    attributes = {
        'name': 'member',
        'id': 'yes-mem',
        'value': 'Yes'
    }

    band_member = forms.BooleanField(widget=forms.CheckboxInput(attrs=attributes))

    def save(self):
        user = super(AddStudentForm, self).save(commit=commit)
        user.first_name = self.cleaned_data['firstname']
        user.last_name = self.cleaned_data['lastname']
        user.save()

        student = Student()
        student.year = self.cleaned_data['year']
        student.section = self.cleaned_data['section']
        student.address = self.cleaned_data['address']
        student.guardian_firstname = self.cleaned_data['gfirstname']
        student.guardian_lastname = self.cleaned_data['glastname']
        student.guardian_address = self.cleaned_data['gaddress']
        student.guardian_contact = self.cleaned_data['gcontact']
        student.bandMem = self.cleaned_data['band_member']
        student.sibling = self.cleaned_data['sibling']
        student.scholarship = self.cleaned_data['scholarship']
        student.user = user
        student.save()