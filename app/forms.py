from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class UserFormCreation(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': ('First Name')})
        self.fields['last_name'].widget.attrs.update({'placeholder': ('Last Name')})
        self.fields['username'].widget.attrs.update({'placeholder': ('Username')})
        self.fields['email'].widget.attrs.update({'placeholder': ('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder': ('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder': ('Repeat password')})

class ProfileRegisterForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].widget.attrs.update({'placeholder': ('Phone #')})

class TripForm(forms.Form):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        required=True
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        required=True
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        required=True
    )
    days = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
        required=True
    )
    
    
        
class GuideForm(forms.Form):
    profile_pic = forms.ImageField(required=False)
    bio = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-input'})
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
