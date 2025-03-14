from django import forms
from .models import User
from web.models import Department,Semester
from registration.forms import RegistrationForm

class CustomRegistrationForm(RegistrationForm):
    usertype = forms.ChoiceField(
        choices=[("student", "Student"), ("faculty", "Faculty")],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    full_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Full Name"})
    )
    id_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "ID Number"})
    )
    register_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Register Number"})
    )
    semester = forms.ModelChoiceField(
        queryset=Semester.objects.all(),
        required=False,
        empty_label="Select Semester",  # Adds a placeholder-like option
        widget=forms.Select(attrs={"class": "form-control"})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        empty_label="Select Department",  # Adds a placeholder-like option
        widget=forms.Select(attrs={"class": "form-control"})
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username"})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"})
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Password"})
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = [
            "usertype", "full_name", "id_number", "register_number", "semester", "department",
            "username", "email", "password1", "password2"
        ]
