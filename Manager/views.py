from django.shortcuts import render
from .models import Doctor, Surgery
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from .forms import PatientForm, SurgeryForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def index(request):
    return render(request, 'Manager/index.html')

@login_required
def doctor_list(request):
    doctors = Doctor.objects.select_related('department').all()
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



@login_required
def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пациент успешно обновлён.')
            return redirect('patient_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'Manager/patient_form.html', {'form': form})

@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Пациент успешно удалён.')
        return redirect('patient_list')
    return render(request, 'Manager/patient_confirm_delete.html', {'patient': patient})



@login_required
def surgery_list(request):
    surgeries = Surgery.objects.all()
    return render(request, 'Manager/surgery_list.html', {'surgeries': surgeries})

@login_required
def surgery_create(request):
    if request.method == 'POST':
        form = SurgeryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Операция успешно добавлена.')
            return redirect('surgery_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SurgeryForm()
    return render(request, 'Manager/surgery_form.html', {'form': form})

@login_required
def surgery_update(request, pk):
    surgery = get_object_or_404(Surgery, pk=pk)
    if request.method == 'POST':
        form = SurgeryForm(request.POST, instance=surgery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Операция успешно обновлена.')
            return redirect('surgery_list')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = SurgeryForm(instance=surgery)
    return render(request, 'Manager/surgery_form.html', {'form': form})

@login_required
def surgery_delete(request, pk):
    surgery = get_object_or_404(Surgery, pk=pk)
    if request.method == 'POST':
        surgery.delete()
        messages.success(request, 'Операция успешно удалена.')
        return redirect('surgery_list')
    return render(request, 'Manager/surgery_confirm_delete.html', {'surgery': surgery})
