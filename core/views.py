from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core import mixins
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from core import forms

from web.models import Department, Semester, Subject, Note, Commend
from core import tables

from django.contrib.auth import get_user_model

User = get_user_model()


@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_id = data.get("user_id")
            content = data.get("content")

            user = User.objects.get(id=user_id)
            message = Commend.objects.create(user=user, content=content, is_active=True)

            return JsonResponse({"success": True, "message_id": message.id})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"})


class HomeView(mixins.FormView):
    template_name = "core/home.html"
    form_class = forms.DepartmentForm
    success_url = "/core/"  # Redirect URL after successful form submission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.filter(is_active=True)
        context["semesters"] = Semester.objects.filter(is_active=True)
        return context

    def form_valid(self, form):
        form.save()  # Save the department
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class DepartmentCreateView(mixins.HybridCreateView):
    template_name = "core/home.html"
    model = Department
    fields = "__all__"
    permissions = ("is_superuser", "faculty")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "New Department"
        return context


class DepartmentUpdateView(mixins.HybridUpdateView):
    template_name = "web/partials/object_form.html"
    model = Department
    fields = "__all__"
    permissions = ("is_superuser", 'faculty')
    

class DepartmentDeleteView(mixins.HybridDeleteView):
    template_name = "web/partials/object_delete.html"
    model = Department
    
    
class SemesterListView(mixins.HybridListView, mixins.FormView):
    template_name = "web/semester.html"
    model = Semester
    form_class = forms.SemesterForm
    filterset_fields = {'name': ['exact']}
    table_class = tables.SemesterTable
    permissions = ("is_superuser",)
    success_url = "/core/semesters/"

    def get_queryset(self):
        queryset = Semester.objects.filter(is_active=True)
        department_id = self.request.GET.get("department_id")
        if department_id:
            queryset = queryset.filter(department_id=department_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department_id = self.request.GET.get("department_id")
        context["title"] = "Semesters"
        context["semesters"] = self.get_queryset()
        context["form"] = forms.SemesterForm
        context["selected_department"] = department_id
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    

class SemesterUpdateView(mixins.HybridUpdateView):
    template_name = "web/partials/object_form.html"
    model = Semester
    fields = "__all__"
    permissions = ("is_superuser", 'faculty')
    

class SemesterDeleteView(mixins.HybridDeleteView):
    template_name = "web/partials/object_delete.html"
    model = Semester
    

class SubjectListView(mixins.HybridListView, mixins.FormView):
    template_name = "web/subject.html"
    form_class = forms.SubjectForm
    model = Subject
    filterset_fields = {'name': ['exact']}
    permissions = ("is_superuser",)

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter by department if provided
        department_pk = self.kwargs.get("department_pk")
        if department_pk:
            queryset = queryset.filter(department__pk=department_pk)

        # Filter by semester if provided
        semester_pk = self.kwargs.get("semester_pk")
        if semester_pk:
            queryset = queryset.filter(semester__pk=semester_pk)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get semester_pk from URL
        semester_pk = self.kwargs.get("semester_pk")

        # Filter subjects and related notes based on semester
        context["subjects"] = self.get_queryset()
        context["notes"] = Note.objects.filter(subject__semester__pk=semester_pk) if semester_pk else Note.objects.none()
        context["semester_name"] = Semester.objects.get(pk=semester_pk).name if semester_pk else None
        context["department_name"] = Department.objects.get(pk=self.kwargs.get("department_pk")).name if self.kwargs.get("department_pk") else None
        # Add the form to context for rendering
        context["form"] = self.get_form()

        return context

    def form_valid(self, form):
        # Save the new Subject instance
        new_subject = form.save(commit=False)
        
        # Ensure the semester and department are set before saving (if they aren't set by the form)
        department_pk = self.kwargs.get("department_pk")
        semester_pk = self.kwargs.get("semester_pk")

        # Optionally set department and semester if they're not included in the form fields
        if department_pk:
            new_subject.department = Department.objects.get(pk=department_pk)
        if semester_pk:
            new_subject.semester = Semester.objects.get(pk=semester_pk)

        # Save the subject
        new_subject.save()

        # Redirect to success URL after saving
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy(
            "core:subject_list",
            kwargs={
                "semester_pk": self.kwargs.get("semester_pk"),  # Retrieve from URL parameters
                "department_pk": self.kwargs.get("department_pk")
            }
        )


class SubjectDetailView(mixins.HybridDetailView):
    template_name = "web/subject_detail.html"
    model = Subject
    permissions = ("is_superuser")
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)

        semester_pk = self.kwargs.get("semester_pk")
        if semester_pk:
            queryset = queryset.filter(semester_id=semester_pk)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Subjects"
        context["subjects"] = self.get_queryset() 
        return context
    

class SubjectUpdateView(mixins.HybridUpdateView):
    template_name = "web/partials/object_form.html"
    model = Subject
    fields = "__all__"
    permissions = ("is_superuser", 'faculty')
    

class SubjectDeleteView(mixins.HybridDeleteView):
    template_name = "web/partials/object_delete.html"
    model = Subject
    
    
class NoteListView(mixins.HybridListView, mixins.FormView):
    template_name = "web/note.html"
    model = Note
    form_class = forms.NoteForm
    filterset_fields = {'name': ['exact']}
    permissions = ("is_superuser",)

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)  # Avoid assigning to self.object_list
        subject_pk = self.kwargs.get("subject_pk")
        if subject_pk:
            queryset = queryset.filter(subject_id=subject_pk)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Don't pass object_list explicitly
        context["title"] = "Notes"
        context["notes"] = self.get_queryset()
        context["form"] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse_lazy(
            "core:note_list",
            kwargs={
                "subject_pk": self.kwargs.get("subject_pk"),  # Retrieve from URL parameters
            }
        )

class NoteUpdateView(mixins.HybridUpdateView):
    template_name = "web/partials/object_form.html"
    model = Note
    fields = "__all__"
    permissions = ("is_superuser", 'faculty')
    

class NoteDeleteView(mixins.HybridDeleteView):
    template_name = "web/partials/object_delete.html"
    model = Note

    
class CommendView(mixins.HybridListView):
    template_name = "web/commend.html"

    def get(self, request, subject_pk):
        """Fetch and display all messages for a specific subject."""
        messages = Commend.objects.filter(subject_id=subject_pk).select_related("user")
        return render(request, self.template_name, {"messages": messages, "subject_pk": subject_pk})

    def post(self, request, subject_pk):
        """Save new messages when users send them."""
        message_text = request.POST.get("message", "").strip()

        if message_text:
            Commend.objects.create(
                subject_id=subject_pk,
                user=request.user,
                message=message_text
            )

        return JsonResponse({"status": "success", "message": message_text, "user": request.user.username})
    