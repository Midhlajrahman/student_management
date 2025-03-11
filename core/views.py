from django.urls import reverse_lazy

from core import mixins

from web.models import Department

class HomeView(mixins.TemplateView):
    template_name = "core/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        return context
    
     
    
