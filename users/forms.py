from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1']

class UserUpdateForm(forms.ModelForm):
    # username=forms.CharField(max_length=20,required=False)
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image','category']