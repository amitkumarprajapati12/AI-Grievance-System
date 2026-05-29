from django.shortcuts import render, redirect

from .forms import GrievanceForm

from .models import Grievance


def detect_category(text):

    text = text.lower()

    if "wifi" in text or "server" in text:
        return "Technical"

    elif "teacher" in text or "exam" in text:
        return "Academic"

    elif "hostel" in text or "room" in text:
        return "Hostel"

    else:
        return "Other"


def home(request):

    return render(
        request,
        'home.html'
    )


def submit_grievance(request):

    if request.method == 'POST':

        form = GrievanceForm(request.POST)

        if form.is_valid():

            grievance = form.save(commit=False)

            grievance.category = detect_category(
                grievance.complaint
            )

            grievance.save()

            return redirect('success')

    else:

        form = GrievanceForm()

    return render(
        request,
        'submit.html',
        {'form': form}
    )


def success(request):

    return render(
        request,
        'success.html'
    )