# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def login_view(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("patients:dashboard")
        else:
            context["error"] = "Invalid credentials"
    return render(request, "patients/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("patients:login")


@login_required
def dashboard_view(request):
    # For now, placeholder — patient table + chart will go here
    return render(request, "patients/dashboard.html")
