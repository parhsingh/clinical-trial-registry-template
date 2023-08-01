from django.db import models
from django.conf import settings
import datetime

from userauth.models import PrimaryRegistry, SecondaryRegistry
primaryRegistryChoices = [(registry.name, registry.name) for registry in PrimaryRegistry.objects.all()]
secondaryRegistryChoices = [(registry.name, registry.name) for registry in SecondaryRegistry.objects.all()]

class ClinicalTrial(models.Model):
    # Auto Input
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    date_of_registration_primary_registry = models.DateField(default=datetime.date.today)
    
    # Primary Registry
    primary_registry_name = models.CharField(max_length=255, choices=primaryRegistryChoices, default='ICMR')
    primary_registry_identifying_number = models.CharField(max_length=255, unique=True, blank=True)

    # Secondary Registry
    secondary_registry_name = models.CharField(max_length=255, choices=secondaryRegistryChoices, default='ICMR', blank=True, null=True)
    secondary_registry_identifying_number = models.CharField(max_length=255, default='SecondaryRegistry/Trial/007', blank=True, null=True)
    
    # Monetary Support
    source_of_monetary_or_material_support = models.TextField(default='test')
    
    # Primary Sponsor
    primary_sponsor_name = models.CharField(max_length=500, default='test')
    primary_sponsor_email = models.EmailField(default='test@test.com')
    primary_sponsor_address = models.TextField(default='test')
    
    # Secondary Sponsor
    secondary_sponsor_name = models.CharField(max_length=255, default='test', blank=True, null=True)
    secondary_sponsor_email = models.EmailField(default='test@test.com', blank=True, null=True)
    secondary_sponsor_address = models.TextField(default='test', blank=True, null=True)
 
    # Post Graduate Thesis
    post_graduate_thesis_check = models.CharField(max_length=255, choices=[("Yes", "Yes"), ("No", "No")], default='test')
    post_graduate_thesis = models.CharField(max_length=100, default='test')
    
    # Public Query Contact
    public_query_contact_name = models.CharField(max_length=255, default='test')
    public_query_contact_phone = models.CharField(max_length=20, default='test')
    public_query_contact_email = models.EmailField(default='test@test.com')
    public_query_contact_address = models.TextField(default='test')
    
    # Scientific Query Contact
    scientific_query_contact_name_and_title = models.CharField(max_length=255, default='test')
    scientific_query_contact_phone = models.CharField(max_length=20, default='test')
    scientific_query_contact_email = models.EmailField(default='test@test.com')
    scientific_query_contact_address = models.TextField(default='test')
    
    # Principal Investigator Contact
    principal_investigator_name = models.CharField(max_length=255, default='test')
    principal_investigator_address = models.TextField(default='test')
    principal_investigator_phone = models.CharField(max_length=20, default='test')
    principal_investigator_email = models.EmailField(default='test@test.com')
    
    # Titles of Study
    public_title_of_study = models.CharField(max_length=255, default='test')
    scientific_title_of_study = models.CharField(max_length=255, default='test')
    
    # Countries of Recruitment
    countries_of_recruitment = models.TextField(default='test')
    
    # Health Conditions Studied
    health_conditions_studied = models.TextField(default='test')
    
    # Intervention Details
    intervention_name = models.CharField(max_length=350, default='test')
    intervention_description = models.TextField(default='test')
 
    # Inclusion and Exclusion Criteria
    inclusion_criteria = models.TextField(default='test')
    exclusion_criteria = models.TextField(default='test')
    
    # Study Type/Design
    type_of_study = models.CharField(max_length=255, choices=[("Interventional", "Interventional"), ("Observational", "Observational")], default='Interventional')
    method_of_allocation = models.CharField(max_length=255, choices=[("Randomized", "Randomized"), ("Non-Randomized", "Non-Randomized"), ("NA: Single Arm Study", "NA: Single Arm Study")], default='Randomized')
    masking_used = models.CharField(max_length=255, choices=[("Y", "Yes, used"), ("N", "No, not used")], default='Y')
    masking_description = models.CharField(max_length=255, default='test', null=True, blank=True)
    assignment = models.CharField(max_length=255, choices=[("Parallel", "Parallel"), ("Cross Over", "Cross Over"), ("Factorial", "Factorial"), ("NA: Single Arm Study", "NA: Single Arm Study")], default='Parallel')
    purpose = models.CharField(max_length=255, default='test')
    phase = models.CharField(max_length=255, choices=[("NA", "NA"), ("0", "0 (Exploratory Trials)"), ("1", "1"), ("1-2", "1-2"), ("2", "2"), ("2-3", "2-3"), ("3", "3"), ("4", "4")], blank=True, null=True)

    # Dates of First Enrollments
    date_of_first_enrollment_india = models.DateField(default=datetime.date.today)
    date_of_first_enrollment_global = models.DateField(null=True, blank=True)
    
    # Sample Size
    target_sample_size = models.PositiveIntegerField(default=0)
    final_enrollment_sample_size = models.PositiveIntegerField(default=0)
    recruitment_status_india = models.CharField(max_length=255, choices=[("Pending", "Pending: Participants are not yet being recruited or enrolled at any site"), ("Recruiting", "Recruiting: Participants are currently being recruited and enrolled"), ("Suspended", "Suspended: There is a temporary halt in recruitment and enrollment"), ("Completed", "Completed: Participants are no longer being recruited or enrolled"), ("Other", "Other")], default='----')
    recruitment_status_global = models.CharField(max_length=255, choices=[("Pending", "Pending: Participants are not yet being recruited or enrolled at any site"), ("Recruiting", "Recruiting: Participants are currently being recruited and enrolled"), ("Suspended", "Suspended: There is a temporary halt in recruitment and enrollment"), ("Completed", "Completed: Participants are no longer being recruited or enrolled"), ("Other", "Other")], default='----')

    # Site of Study
    sites_of_study = models.TextField(default='test')
    sites_of_study_phone = models.TextField(default='test')
    sites_of_study_email = models.TextField(default='test')
    sites_of_study_address = models.TextField(default='test')

    # Primary Outcome
    primary_outcome_1 = models.CharField(max_length=255, default='test')
    primary_outcome_metric_1 = models.TextField(default='test')
    primary_outcome_timepoint_1 = models.CharField(max_length=500, default='test')
    primary_outcome_2 = models.CharField(max_length=500, default='test', null=True, blank=True)
    primary_outcome_metric_2 = models.TextField(default='test', null=True, blank=True)
    primary_outcome_timepoint_2 = models.CharField(max_length=255, default='test', null=True, blank=True)
    primary_outcome_3 = models.CharField(max_length=255, default='test', null=True, blank=True)
    primary_outcome_metric_3 = models.TextField(default='test', null=True, blank=True)
    primary_outcome_timepoint_3 = models.CharField(max_length=255, default='test', null=True, blank=True)

    # Secondary Outcomes
    secondary_outcome_1 = models.CharField(max_length=255, default='test', null=True, blank=True)
    secondary_outcome_metric_1 = models.TextField(default='test', null=True, blank=True)
    secondary_outcome_timepoint_1 = models.CharField(max_length=255, default='test', null=True, blank=True)
    secondary_outcome_2 = models.CharField(max_length=255, default='test', null=True, blank=True)
    secondary_outcome_metric_2 = models.TextField(default='test', null=True, blank=True)
    secondary_outcome_timepoint_2 = models.CharField(max_length=255, default='test', null=True, blank=True)
    secondary_outcome_3 = models.CharField(max_length=255, default='test', null=True, blank=True)
    secondary_outcome_metric_3 = models.TextField(default='test', null=True, blank=True)
    secondary_outcome_timepoint_3 = models.CharField(max_length=255, default='test', null=True, blank=True)

    # Ethics Review
    ethics_committee_approval_status = models.CharField(max_length=255, choices=[("Not Approved", "Not Approved"), ("Approved", "Approved"), ("Not Available", "Not Available")], default='----')
    ethics_committee_date_of_approval = models.DateField(default=datetime.date.today)
    ethics_committee_name = models.CharField(max_length=255, default='test')
    ethics_committee_phone = models.CharField(max_length=255, default='test')
    ethics_committee_email = models.CharField(max_length=255, default='test')
    ethics_committee_address = models.TextField(default='test')

    # Date of Completion
    date_of_study_completion = models.DateField(default=datetime.date.today)

    # Summary Results
    date_of_posting_results = models.DateField(default=datetime.date.today)
    date_of_first_jounal_publication = models.DateField(default=datetime.date.today)
    urls_related_to_results = models.TextField(default='test')
    baseline_characteristics = models.TextField(default='test')
    participant_flow = models.TextField(default='test')
    adverse_events = models.TextField(default='test')
    outcome_measures = models.TextField(default='test')
    protocol_files = models.TextField(default='test')
    brief_summary = models.TextField(default='test')

    # Data Sharing Plan
    data_shared = models.CharField(max_length=255, choices=[("Yes", "Yes"), ("No", "No"), ("Undecided", "Undecided")], default='----')
    data_sharing_plan = models.TextField(default='test')

    # Additional Optional Data
    lay_summary = models.TextField(default='test', null=True, blank=True)
    approvals = models.TextField(default='test', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.primary_registry_identifying_number:
            last_id = ClinicalTrial.objects.order_by('-id').first()
            last_id_number = 0
            if last_id and last_id.primary_registry_identifying_number:
                last_id_number = int(last_id.primary_registry_identifying_number.split('/')[-1])
            
            new_id_number = last_id_number + 1

            self.primary_registry_identifying_number = f"CTRI/ClinicalTrial/{new_id_number}"

        if not self.pk:
            self.date_of_registration_primary_registry = datetime.date.today()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.primary_registry_identifying_number