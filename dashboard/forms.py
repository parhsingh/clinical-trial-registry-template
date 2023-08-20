from django import forms
from .models import ClinicalTrial

class ClinicalTrialForm(forms.ModelForm):
    class Meta:
        model = ClinicalTrial
        fields = '__all__'
        exclude = ['primary_registry_name', 'primary_registry_identifying_number', 'date_of_registration_primary_registry']
        widgets = {
            'secondary_registry_name': forms.Select(attrs={'placeholder': 'Select Secondary Registry'}),
            'secondary_registry_identifying_number': forms.Textarea(attrs={'placeholder': 'Enter Secondary Registery ID(s) (UTN, Sponsor Assigned etc.)', 'rows': 3}),

            'source_of_monetary_or_material_support': forms.Textarea(attrs={'placeholder': 'Major source(s) of monetary or material support for the trial (funding agency, foundation, company, institution etc.)', 'rows': 3}),

            'primary_sponsor_name': forms.TextInput(attrs={'placeholder': "Enter Primary Sponsor's Name"}),
            'primary_sponsor_email': forms.TextInput(attrs={'placeholder': "Enter Primary Sponsor's Email"}),
            'primary_sponsor_address': forms.Textarea(attrs={'placeholder': "Enter Primary Sponsor's Address", 'rows': 3}),

            'secondary_sponsor_name': forms.TextInput(attrs={'placeholder': "Enter Secondary Sponsor's Name"}),
            'secondary_sponsor_email': forms.TextInput(attrs={'placeholder': "Enter Secondary Sponsor's Email"}),
            'secondary_sponsor_address': forms.Textarea(attrs={'placeholder': "Enter Secondary Sponsor's Address", 'rows': 3}),

            'post_graduate_thesis_check': forms.Select(attrs={'placeholder': 'Enter Post Graduate Thesis Check'}),
            'post_graduate_thesis': forms.TextInput(attrs={'placeholder': 'Enter Post Graduate Thesis'}),

            'public_query_contact_name': forms.TextInput(attrs={'placeholder': 'Enter Public Query Contact Name'}),
            'public_query_contact_phone': forms.TextInput(attrs={'placeholder': 'Enter Public Query Contact Phone'}),
            'public_query_contact_email': forms.EmailInput(attrs={'placeholder': 'Enter Public Query Contact Email'}),
            'public_query_contact_address': forms.Textarea(attrs={'placeholder': 'Enter Public Query Contact Address', 'rows': 3}),
            
            'scientific_query_contact_name_and_title': forms.TextInput(attrs={'placeholder': 'Enter Scientific Query Contact Name and Title'}),
            'scientific_query_contact_phone': forms.TextInput(attrs={'placeholder': 'Enter Scientific Query Contact Phone'}),
            'scientific_query_contact_email': forms.EmailInput(attrs={'placeholder': 'Enter Scientific Query Contact Email'}),
            'scientific_query_contact_address': forms.Textarea(attrs={'placeholder': 'Enter Scientific Query Contact Address', 'rows': 3}),

            'principal_investigator_name': forms.TextInput(attrs={'placeholder': 'Enter Principal Investigator Name'}),
            'principal_investigator_address': forms.Textarea(attrs={'placeholder': 'Enter Principal Investigator Address', 'rows': 3}),
            'principal_investigator_phone': forms.TextInput(attrs={'placeholder': 'Enter Principal Investigator Phone'}),
            'principal_investigator_email': forms.EmailInput(attrs={'placeholder': 'Enter Principal Investigator Email'}),

            'public_title_of_study': forms.TextInput(attrs={'placeholder': 'Enter Public Title of Study'}),
            'scientific_title_of_study': forms.TextInput(attrs={'placeholder': 'Enter Scientific Title of Study'}),

            'countries_of_recruitment': forms.Textarea(attrs={'placeholder': 'Enter Countries of Recruitment', 'rows': 3}),

            'health_conditions_studied': forms.Textarea(attrs={'placeholder': 'Enter Health Condition(s) or Problem(s) studied'}),

            'intervention_name': forms.TextInput(attrs={'placeholder': 'Enter Intervention Name'}),
            'intervention_description': forms.Textarea(attrs={'placeholder': 'Enter Intervention Description', 'rows': 3}),

            'inclusion_criteria': forms.Textarea(attrs={'placeholder': 'Enter Inclusion Criteria', 'rows': 3}),
            'exclusion_criteria': forms.Textarea(attrs={'placeholder': 'Enter Exclusion Criteria', 'rows': 3}),

            'type_of_study': forms.Select(attrs={'placeholder': 'Enter Type of Study'}),
            'method_of_allocation': forms.Select(attrs={'placeholder': 'Enter Method of Allocation'}),
            'masking_used': forms.Select(attrs={'placeholder': 'Is masking used?'}),
            'masking_description': forms.TextInput(attrs={'placeholder': 'Enter who is masked', 'rows': 3}),
            'assignment': forms.Select(),
            'purpose': forms.TextInput(attrs={'placeholder': 'Enter Purpose of Study'}),
            'phase': forms.Select(),

            'date_of_first_enrollment_india': forms.DateInput(attrs={'placeholder': 'Enter Date of First Enrollment (India)'}),
            'date_of_first_enrollment_global': forms.DateInput(attrs={'placeholder': 'Enter Date of First Enrollment (Global)'}),

            'target_sample_size': forms.TextInput(attrs={'placeholder': 'Enter Target Sample Size'}),
            'final_enrollment_sample_size': forms.TextInput(attrs={'placeholder': 'Enter Final Enrollment Sample Size'}),
            'recruitment_status_india': forms.Select(),
            'recruitment_status_global': forms.Select(),

            'sites_of_study': forms.Textarea(attrs={'placeholder': 'Enter Site of Study', 'rows': 3}),
            'sites_of_study_phone': forms.Textarea(attrs={'placeholder': 'Enter Site of Study Phone', 'rows': 3}),
            'sites_of_study_email': forms.Textarea(attrs={'placeholder': 'Enter Site of Study Email', 'rows': 3}),
            'sites_of_study_address': forms.Textarea(attrs={'placeholder': 'Enter Site of Study Address', 'rows': 3}),

            'primary_outcome_1': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome 1'}),
            'primary_outcome_metric_1': forms.Textarea(attrs={'placeholder': 'Enter Primary Outcome Metric 1'}),
            'primary_outcome_timepoint_1': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome Timepoint 1'}),
            'primary_outcome_2': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome 2'}),
            'primary_outcome_metric_2': forms.Textarea(attrs={'placeholder': 'Enter Primary Outcome Metric 2'}),
            'primary_outcome_timepoint_2': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome Timepoint 2'}),
            'primary_outcome_3': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome 3'}),
            'primary_outcome_metric_3': forms.Textarea(attrs={'placeholder': 'Enter Primary Outcome Metric 3'}),
            'primary_outcome_timepoint_3': forms.TextInput(attrs={'placeholder': 'Enter Primary Outcome Timepoint 3'}),

            'secondary_outcome_1': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome 1'}),
            'secondary_outcome_metric_1': forms.Textarea(attrs={'placeholder': 'Enter Secondary Outcome Metric 1'}),
            'secondary_outcome_timepoint_1': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome Timepoint 1'}),
            'secondary_outcome_2': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome 2'}),
            'secondary_outcome_metric_2': forms.Textarea(attrs={'placeholder': 'Enter Secondary Outcome Metric 2'}),
            'secondary_outcome_timepoint_2': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome Timepoint 2'}),
            'secondary_outcome_3': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome 3'}),
            'secondary_outcome_metric_3': forms.Textarea(attrs={'placeholder': 'Enter Secondary Outcome Metric 3'}),
            'secondary_outcome_timepoint_3': forms.TextInput(attrs={'placeholder': 'Enter Secondary Outcome Timepoint 3'}),

            'ethics_committee_approval_status': forms.Select(),
            'ethics_committee_date_of_approval': forms.DateInput(attrs={'placeholder': 'Enter Ethics Committee Date of Approval'}),
            'ethics_committee_name': forms.TextInput(attrs={'placeholder': 'Enter Ethics Committee Name'}),
            'ethics_committee_phone': forms.TextInput(attrs={'placeholder': 'Enter Ethics Committee Phone'}),
            'ethics_committee_email': forms.EmailInput(attrs={'placeholder': 'Enter Ethics Committee Email'}),
            'ethics_committee_address': forms.Textarea(attrs={'placeholder': 'Enter Ethics Committee Address', 'rows': 3}),

            'date_of_study_completion': forms.DateInput(attrs={'placeholder': 'Enter Date of Study Completion'}),

            'date_of_posting_results': forms.DateInput(attrs={'placeholder': 'Enter Date of Posting Results'}),
            'date_of_first_jounal_publication': forms.DateInput(attrs={'placeholder': 'Enter Date of First Journal Publication'}),
            'urls_related_to_results': forms.Textarea(attrs={'placeholder': 'Enter URLs related to Results', 'rows': 3}),
            'baseline_characteristics': forms.Textarea(attrs={'placeholder': 'Enter Baseline Characteristics', 'rows': 3}),
            'participant_flow': forms.Textarea(attrs={'placeholder': 'Enter Participant Flow', 'rows': 3}),
            'adverse_events': forms.Textarea(attrs={'placeholder': 'Enter Adverse Events', 'rows': 3}),
            'outcome_measures': forms.Textarea(attrs={'placeholder': 'Enter Outcome Measures', 'rows': 3}),
            'protocol_files': forms.Textarea(attrs={'placeholder': 'Enter Protocol Files', 'rows': 3}),
            'brief_summary': forms.Textarea(attrs={'placeholder': 'Enter Brief Summary', 'rows': 3}),

            'data_shared': forms.Select(),
            'data_sharing_plan': forms.Textarea(attrs={'placeholder': 'Enter Data Sharing Plan', 'rows': 3}),

            'lay_summary': forms.Textarea(attrs={'placeholder': 'Enter Lay Summary', 'rows': 3}),
            'approvals': forms.Textarea(attrs={'placeholder': 'Enter Approvals', 'rows': 3}),
        }