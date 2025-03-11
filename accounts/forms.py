from django import forms
from registration.forms import RegistrationForm

from .models import User


class CustomRegistrationForm(RegistrationForm):
    usertype = forms.ChoiceField(
        choices=[("student", "Student"), ("faculty", "Faculty")],
        initial="student",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    full_name = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    id_number = forms.CharField(max_length=128, required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    department = forms.CharField(max_length=128, required=True, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["usertype", "full_name", "id_number", "department", "username", "email", "password1", "password2",]