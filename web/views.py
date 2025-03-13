from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {"is_index": True}
    return render(request, "web/index.html", context)



def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)


def service(request):
    context = {"is_service": True}
    return render(request, "web/service.html", context)

