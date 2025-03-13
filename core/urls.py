from django.urls import path

from . import views


app_name = "core"

urlpatterns = [
    path("send-message/", views.send_message, name="send_message"),
    path("", views.HomeView.as_view(), name="home"),
    path("new/department/", views.DepartmentCreateView.as_view(), name="department_create"),
    path("new/<int:pk>/department/", views.DepartmentCreateView.as_view(), name="department_create"),
    path("update/<int:pk>/department/", views.DepartmentUpdateView.as_view(), name="department_update"),
    path("delete/<int:pk>/department/", views.DepartmentDeleteView.as_view(), name="department_delete"),
    path("semesters/", views.SemesterListView.as_view(), name="semester_list"),
    path("update/<int:pk>/semester/", views.SemesterUpdateView.as_view(), name="semester_update"),
    path("delete/<int:pk>/semester/", views.SemesterDeleteView.as_view(), name="semester_delete"),
    path("subjects/<int:semester_pk>/<int:department_pk>/", views.SubjectListView.as_view(), name="subject_list"),
    path("subject/<int:pk>/", views.SubjectDetailView.as_view(), name="subject_detail"),
    path("subject/<int:pk>/update/", views.SubjectUpdateView.as_view(), name="subject_update"),
    path("subject/<int:pk>/delete/", views.SubjectDeleteView.as_view(), name="subject_delete"),
    path("notes/<int:subject_pk>/", views.NoteListView.as_view(), name="note_list"),
    path("note/<int:pk>/update/", views.NoteUpdateView.as_view(), name="note_update"),
    path("note/<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note_delete"),
    path("commends/<int:subject_pk>/", views.CommendView.as_view(), name="commend_list"),
    ]
