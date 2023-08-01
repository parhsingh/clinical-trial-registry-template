from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClinicalTrialForm
from django.contrib import messages
from .models import ClinicalTrial
import datetime

@login_required(login_url="/login")
def dashboard_view(request):
    user = request.user
    notifications = messages.get_messages(request)

    try:
        registeredTrials = ClinicalTrial.objects.filter(user=user)
    except ClinicalTrial.DoesNotExist:
        registeredTrials = None

    context = {
        "user": user,
        "registeredTrials": registeredTrials,
        "notifications": notifications
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="/login")
def register_trial(request):
    if request.method == "POST":
        form = ClinicalTrialForm(request.POST)
        if form.is_valid():
            clinical_trial = form.save(commit=False)
            clinical_trial.user = request.user
            clinical_trial.date_of_registration_primary_registry = datetime.date.today()
            clinical_trial.save()
            messages.success(request, "Clinical trial registered successfully!")
            return redirect("/dashboard")
    else:
        form = ClinicalTrialForm()

    user = request.user
    context = {"user": user, "form": form}
    return render(request, "registertrial.html", context)