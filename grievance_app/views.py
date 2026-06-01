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


def detect_priority(text):
    text = text.lower()

    high_words = [
        "urgent",
        "emergency",
        "fire",
        "accident",
        "danger",
        "serious",
        "immediate",
        "help",
        "medical",
        "injury"
    ]

    medium_words = [
        "wifi",
        "internet",
        "server",
        "exam",
        "marks",
        "teacher",
        "hostel",
        "room",
        "mess",
        "water",
        "electricity"
    ]

    for word in high_words:
        if word in text:
            return "High"

    for word in medium_words:
        if word in text:
            return "Medium"

    return "Low"


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

            grievance.priority = detect_priority(grievance.complaint)

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

    total_count = complaints.count()
    pending_count = complaints.filter(status='Pending').count()
    resolved_count = complaints.filter(status='Resolved').count()
    rejected_count = complaints.filter(status='Rejected').count()

    return render(request, 'dashboard.html', {
        'complaints': complaints,
        'total_count': total_count,
        'pending_count': pending_count,
        'resolved_count': resolved_count,
        'rejected_count': rejected_count,
    })


def track_complaint(request):
    complaint = None
    error = None

    if request.method == 'POST':
        tracking_id = request.POST.get('tracking_id')

        try:
            complaint = Grievance.objects.get(tracking_id=tracking_id)
        except Grievance.DoesNotExist:
            error = "No complaint found with this Tracking ID."

    return render(request, 'track.html', {
        'complaint': complaint,
        'error': error
    })


def logout_user(request):
    logout(request)
    return redirect('home')