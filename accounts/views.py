from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from registration.backends.default.views import RegistrationView

from core import mixins

from . import tables
from .forms import CustomRegistrationForm
from .models import User


class CustomRegistrationView(RegistrationView):
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('web:index')

    def register(self, form):
        user = form.save(commit=False)
        user.full_name = form.cleaned_data['full_name']
        user.usertype = form.cleaned_data['usertype']
        
        if user.usertype == "student":
            user.register_number = form.cleaned_data['register_number']
            user.semester = form.cleaned_data['semester']
        else:
            user.id_number = form.cleaned_data['id_number']

        user.department = form.cleaned_data['department']
        user.save()

        # Authenticate and login user
        user = authenticate(
            self.request, username=form.cleaned_data['username'], password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
        
        return user


class UserListView(mixins.HybridListView):
    model = User
    table_class = tables.UserTable
    filterset_fields = ("is_active", "is_staff")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Users"
        context["can_add"] = True
        context["new_link"] = reverse_lazy("accounts:user_create")
        return context


class UserDetailView(mixins.HybridDetailView):
    model = User


class UserCreateView(mixins.HybridCreateView):
    model = User
    exclude = ("is_active", "date_joined", "user_permissions", "groups", "last_login", "is_superuser", "is_staff")

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data["password"])
        return super().form_valid(form)


class UserUpdateView(mixins.HybridUpdateView):
    model = User
    exclude = (
        "is_active",
        "password",
        "date_joined",
        "user_permissions",
        "groups",
        "last_login",
        "is_superuser",
        "is_staff",
    )


class UserDeleteView(mixins.HybridDeleteView):
    model = User