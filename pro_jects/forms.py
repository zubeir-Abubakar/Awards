from django import forms
from .models import Profile,Project

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    exclude=['projects']

class NewProjectForm(forms.ModelForm):
  class Meta:
    model=Project
    exclude=['user']