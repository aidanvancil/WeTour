from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserFormCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TripForm(forms.Form):
    def validate_four_choices(value):
        if len(value) > 4:
            raise ValidationError('You may select up to four choices.')
        
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
        ('Q3', 'Extrovert'),
        ('Q4', 'Adventurous'),
        ('Q5', 'Daring'),
        ('Q6', 'Calm'),
        ('Q7', 'Nervous'),
        ('Q8', 'Catious'),
        ('Q9', 'Open Minded'),
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
        ('Q3', 'Extrovert'),
        ('Q4', 'Adventurous'),
        ('Q5', 'Daring'),
        ('Q6', 'Calm'),
        ('Q7', 'Nervous'),
        ('Q8', 'Catious'),
        ('Q9', 'Open Minded'),
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