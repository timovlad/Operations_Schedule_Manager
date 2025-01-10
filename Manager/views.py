from django.shortcuts import render
from .models import Doctor
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'Manager/index.html')

@login_required
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'Manager/doctor_list.html', {'doctors': doctors})



@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'Manager/patient_list.html', {'patients': patients})

@login_required
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'Manager/patient_form.html', {'form': form})
