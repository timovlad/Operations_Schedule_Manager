from django.shortcuts import render
from .models import Doctor
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'Manager/index.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Manager/doctor_list.html', {'doctors': doctors})


@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Manager/doctor_list.html', {'doctors': doctors})

