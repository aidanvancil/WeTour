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
    QUALITIES_CHOICES = (
        ('Q1', 'Shy'),
        ('Q2', 'Introvert'),
        ('Q3', 'Adventurous'),
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
    days = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    languages = forms.MultipleChoiceField(
        choices=LANGUAGES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-multiselect'}),
    )
    qualities = forms.MultipleChoiceField(
        choices=QUALITIES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
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
    QUALITIES_CHOICES = (
        ('Q1', 'Shy'),
        ('Q2', 'Introvert'),
        ('Q3', 'Adventurous'),
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
    make = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    model = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    license_plate = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-input'}),
    )
    languages = forms.MultipleChoiceField(
        choices=LANGUAGES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-multiselect'}),
    )
    qualities = forms.MultipleChoiceField(
        choices=QUALITIES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-checkbox'}),
    )

