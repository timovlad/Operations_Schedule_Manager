from django import forms
from django.utils import timezone
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
        widgets = {
            "data_operation": forms.DateTimeInput(attrs={
                "type": "datetime-local",
                "min": timezone.now().strftime("%Y-%m-%dT%H:%M"),
                "step": 3600,
            }),
        }
