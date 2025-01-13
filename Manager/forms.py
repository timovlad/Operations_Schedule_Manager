from .models import Patient, Surgery
from django import forms
from django.forms.widgets import DateTimeInput


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["first_name", "last_name", "doctor", "department", "room_number", "operation"]


class SurgeryForm(forms.ModelForm):
    start_time = forms.DateTimeField(
        label="Дата и время операции",
        input_formats=["%d.%m.%Y %H:%M", "%Y-%m-%d %H:%M"],
        widget=DateTimeInput(attrs={
            "class": "form-control",
            "placeholder": "дд.мм.гггг чч:мм",
        }),
        help_text="Введите дату и время операции в формате дд.мм.гггг чч:мм"
    )

    class Meta:
        model = Surgery
        fields = ["start_time", "surgery_name", "operating_room"]
