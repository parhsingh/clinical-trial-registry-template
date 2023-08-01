from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Organisation

class CreateUserForm(UserCreationForm):
    organisation = forms.ModelChoiceField(queryset=Organisation.objects.all(), empty_label="Select an organisation")

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile_number', 'gender', 'organisation', 'designation', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Enter your mobile number'}),
            'gender': forms.Select(attrs={'placeholder': 'Select your gender'}),
            'designation': forms.TextInput(attrs={'placeholder': 'Enter your Designation'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

class RegisterOrganisation(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Organisation\'s Name'}),
            'official_address': forms.Textarea(attrs={'placeholder': 'Enter Organisation\'s Official Address'}),
            'country': forms.Select(attrs={'placeholder': 'Enter Organisation\'s Country'}),
            'state': forms.Select(attrs={'placeholder': 'Enter Organisation\'s State'}),
            'district': forms.TextInput(attrs={'placeholder': 'Enter Organisation\'s District'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Your username'})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    class Meta:
        fields = ['email']