# forms.py
from django import forms
from .models import Conference

class MeetingForm(forms.ModelForm):
    class Meta:
        model = Conference
        fields = ['title', 'date', 'time', 'location', 'description']
