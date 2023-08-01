from django.shortcuts import render

from dashboard.models import ClinicalTrial
from userauth.models import Organisation

def index(request):
    trialsRegistered = ClinicalTrial.objects.all().count()
    organisationsRegistered = Organisation.objects.all().count()
    context = {
        'trialsRegistered': trialsRegistered,
        'organisationsRegistered': organisationsRegistered
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')