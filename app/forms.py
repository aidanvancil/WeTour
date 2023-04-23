from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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
        self.fields['phone_number'].widget.attrs.update({'placeholder': ('Phone #')})

class TripForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    LANGUAGES_CHOICES = (
        ('EN', 'English'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('DE', 'German'),
    )
    QUALITIES_CHOICES = [
        'Shy',
        'Introvert',
        'Extrovert',
        'Adventurous',
        'Daring',
        'Calm',
        'Nervous',
        'Cautious',
        'Open Minded',
    ]

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    days = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    
    
        
class GuideForm(forms.Form):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    LANGUAGES_CHOICES = (
        ('EN', 'English'),
        ('FR', 'French'),
        ('ES', 'Spanish'),
        ('DE', 'German'),
    )
    
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    state = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    phone_number = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )