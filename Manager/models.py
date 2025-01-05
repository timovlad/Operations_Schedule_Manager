from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_future_date

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Manipulation(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Doctor(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Patient(models.Model):
    first_name = models.CharField(max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    doctor = models.ManyToManyField(Doctor, max_length=100, null=False, blank=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    place=models.IntegerField()
    data_operation=models.DateTimeField(validators=[validate_future_date])
    manipulation=models.ForeignKey(Manipulation, on_delete=models.CASCADE)
    class Meta:
        ordering = ["first_name", "last_name"]
