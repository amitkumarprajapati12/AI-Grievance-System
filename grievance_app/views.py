from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q

from .forms import GrievanceForm, RegisterForm
from .models import Grievance


def detect_category(text):
    text = text.lower()

    if "wifi" in text or "server" in text or "internet" in text:
        return "Technical"

    elif "teacher" in text or "exam" in text or "marks" in text:
        return "Academic"

    elif "hostel" in text or "room" in text or "mess" in text:
        return "Hostel"

    else:
        return "Other"


def home(request):
    return render(request, 'home.html')


@login_required
def submit_grievance(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST, request.FILES)

        if form.is_valid():
            grievance = form.save(commit=False)

            grievance.user = request.user

            if not grievance.email:
                grievance.email = request.user.email

            grievance.category = detect_category(grievance.complaint)

            grievance.save()

            return redirect('dashboard')

    else:
        form = GrievanceForm()

    return render(request, 'submit.html', {'form': form})


def success(request):
    return render(request, 'success.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    complaints = Grievance.objects.filter(
        Q(user=request.user) | Q(email=request.user.email)
    ).order_by('-created_at')

    return render(request, 'dashboard.html', {
        'complaints': complaints
    })


def logout_user(request):
    logout(request)
    return redirect('home')