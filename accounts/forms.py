from django import forms
from .models import User
from registration.forms import RegistrationForm

class CustomRegistrationForm(RegistrationForm):
    usertype = forms.ChoiceField(
        choices=[("student", "Student"), ("faculty", "Faculty")],
        widget=forms.Select(attrs={"class": "form-control"})
    )
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class": "form-control"}))
    id_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    register_number = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    semester = forms.ModelChoiceField(
        queryset=User.objects.all(), required=False, widget=forms.Select(attrs={"class": "form-control"})
    )
    department = forms.ModelChoiceField(
        queryset=User.objects.all(), required=True, widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = [
            "usertype", "full_name", "id_number", "register_number", "semester", "department",
            "username", "email", "password1", "password2"
        ]
