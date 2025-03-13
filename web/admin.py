from django.contrib import admin

from .models import *
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
