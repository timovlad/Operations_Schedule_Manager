# forms.py
from django import forms
from .models import Patient
from .models import Surgery


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'doctor', 'department', 'room_number', 'operation']


class SurgeryForm(forms.ModelForm):
    class Meta:
        model = Surgery
        fields = ['start_time', 'surgery_name', 'operating_room']
