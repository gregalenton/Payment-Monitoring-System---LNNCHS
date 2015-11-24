from django import forms
from models import StudentInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['student_lastname', 'student_firstname', 'student_middlename',
                  'student_birthday', 'student_year', 'student_section',
                  'student_gender', 'student_address', 'student_guardian',
                  'student_guardian_contact', 'student_guardian_address', 'student_scholarship',
                  'student_sibling', 'student_bandMem', 'student_paid', 'student_toPay']



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

# class EditStudentForm(forms.ModelForm):
#     class Meta:
#         model = StudentInfo
#         exclude = ['student_id']
#         fields = ['student_lastname', 'student_firstname', 'student_middlename', 
#                   'student_birthday', 'student_year', 'student_section',
#                  'student_gender', 'student_address']

#     def save(self):
#         student= get_object_or_404(StudentInfo, student_id =self.instance.pk)
#         StudentInfo.objects.filter(student_id = self.instance.pk).update(fields)

#         return student
    #     fields = ['student_lastname', 'student_firstname', 'student_middlename', 
    #              'student_birthday', 'student_year', 'student_section',
    #              'student_gender', 'student_address']

    # attribute = {
    #     'class': 'form-control',
    # }             

    # student_lastname = forms.CharField(required=False)
    # student_firstname = forms.CharField(required=False)
    # student_middlename = forms.CharField(required=False)
    # student_birthday = forms.DateField(required=False)

    # attribute['placeholder'] = 'YEAR_LEVEL'
    # student_year = forms.CharField(
    #     required=False,
    #     widget=forms.Select(
    #         attrs=attribute,
    #         choices=StudentInfo.YEAR_LEVEL
    #     )
    # )
    # attribute['placeholder'] = 'SECTION'
    # student_section = forms.CharField(
    #     required=False,
    #     widget=forms.Select(
    #         attrs=attribute,
    #         choices=StudentInfo.SECTION
    #     )
    # )
    # attribute['placeholder'] = 'GENDER'
    # student_gender = forms.CharField(
    #     required=False,
    #     widget=forms.Select(
    #         attrs=attribute,
    #         choices=StudentInfo.GENDER
    #     )
    # )
    # student_address = forms.CharField(required=False)


class SearchStudentForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['student_lastname']


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
