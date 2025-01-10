from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_free_date


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Doctor(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "doctor"
        verbose_name_plural = "doctors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class OperatingRoom(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Surgery(models.Model):
    start_time = models.DateTimeField(validators=[validate_free_date])
    surgery_name = models.CharField(max_length=100, null=False, blank=False)
    operating_room = models.ForeignKey(OperatingRoom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.surgery_name} on {self.start_time}"


class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    operation = models.ForeignKey(Surgery, on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name", "last_name"]

