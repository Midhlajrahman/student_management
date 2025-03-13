from django.db import models
from core.base import BaseModel
from django.urls import reverse_lazy

# Create your models here.


class Department(BaseModel):
    name = models.CharField(max_length=180)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("core:home")
    
    # def get_absolute_url(self):
    #     return reverse_lazy("web:department_detail", kwargs={"pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("core:department_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:department_delete", kwargs={"pk": self.pk})
    

class Semester(BaseModel):
    department = models.ForeignKey("web.Department", on_delete=models.CASCADE, limit_choices_to={'is_active': True})
    name = models.CharField(max_length=180)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("core:semester_list")
    
    def get_absolute_url(self):
        # Check if department is related to the semester
        if hasattr(self, 'department') and self.department:
            return reverse_lazy("core:subject_list", kwargs={"semester_pk": self.pk, "department_pk": self.department.pk})
        else:
            return reverse_lazy("core:subject_list", kwargs={"semester_pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("core:semester_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:semester_delete", kwargs={"pk": self.pk})


class Subject(BaseModel):
    department = models.ForeignKey("web.Department", on_delete=models.CASCADE)
    semester = models.ForeignKey("web.Semester", on_delete=models.CASCADE)
    name = models.CharField( max_length=180)
    
    def __str__(self):
        return self.name
    
    def get_list_url(self):
        return reverse_lazy("core:subject_list", kwargs={"semester_pk": self.semester.pk, "department_pk": self.department.pk})
    
    def get_absolute_url(self):
        return reverse_lazy("core:subject_detail", kwargs={"pk": self.pk})
    
    def get_note_url(self):
        return reverse_lazy("core:note_list", kwargs={"subject_pk": self.pk})
    
    def get_commend_url(self):
        return reverse_lazy("core:commend_list", kwargs={"subject_pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("core:subject_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:subject_delete", kwargs={"pk": self.pk})
    

class Commend(BaseModel):
    subject = models.ForeignKey("web.Subject", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.commend[:50]}"

    class Meta:
        ordering = ["timestamp"]
    
    @staticmethod
    def get_list_url():
        return reverse_lazy("core:commend_list")
    
    def get_absolute_url(self):
        return reverse_lazy("core:commend_detail", kwargs={"pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("core:commend_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:commend_delete", kwargs={"pk": self.pk})
    

class Note(BaseModel):
    subject = models.ForeignKey("web.Subject", on_delete=models.CASCADE)
    name = models.CharField(max_length=180)
    file = models.FileField(upload_to="note/")
    
    def __str__(self):
        return self.name
    
    def get_list_url(self):
        return reverse_lazy("core:note_list", kwargs={"subject_pk": self.subject.pk,})
    
    def get_absolute_url(self):
        return reverse_lazy("core:note_detail", kwargs={"pk": self.pk})
    
    def get_update_url(self):
        return reverse_lazy("core:note_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:note_delete", kwargs={"pk": self.pk})