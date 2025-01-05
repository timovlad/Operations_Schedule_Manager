from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_future_date(value):
    if value < timezone.now():
        raise ValidationError("Only future dates are allowed.")
    if value.hour < 8 or value.hour >= 16:
        raise ValidationError("Time must be between 8 and 16 hours. Step 1 our")
