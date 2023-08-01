from django.shortcuts import render
from dashboard.models import ClinicalTrial

def search(request):
    trials = ClinicalTrial.objects.all().values("primary_registry_identifying_number", "date_of_registration_primary_registry", "type_of_study", "public_title_of_study", "principal_investigator_name", "principal_investigator_address")
    context = {'trials': trials}
    return render(request, 'search.html', context)
