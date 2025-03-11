from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import USER_TYPE_CHOICES, DEPARTMENT_CHOICES, SEMESTER_CHOICES


class User(AbstractUser):
    usertype = models.CharField(max_length=128, choices=[("student", "Student"), ("faculty", "Faculty")], default="student")
    full_name = models.CharField(max_length=128, blank=True, null=True)
    id_number = models.CharField(max_length=128, blank=True, null=True)
    department = models.CharField(max_length=128,blank=True, null=True)
    
    def get_fields(self):
        return generate_fields(self)

    def get_absolute_url(self):
        return reverse_lazy("accounts:user_detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_list_url():
        return reverse_lazy("accounts:user_list")

    def get_update_url(self):
        return reverse_lazy("accounts:user_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("accounts:user_delete", kwargs={"pk": self.pk})

    @property
    def fullname(self):
        return self.username

    def __str__(self):
        return self.username