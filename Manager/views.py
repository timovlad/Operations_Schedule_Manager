from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from Manager.models import Doctor, Surgery, Patient
from Manager.forms import PatientForm, SurgeryForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(View):
    def get(self, request):
        return render(request, 'Manager/index.html')

class DoctorListView(LoginRequiredMixin, ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'Manager/doctor_list.html'
    queryset = Doctor.objects.select_related('department').all()

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name = 'patients'
    template_name = 'Manager/patient_list.html'
    queryset = Patient.objects.select_related('doctor', 'department', 'operation').all()

class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = "Manager/patient_form.html"
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = "Manager/patient_form.html"
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = "Manager/patient_confirm_delete.html"
    success_url = reverse_lazy('patient_list')

class SurgeryListView(LoginRequiredMixin, ListView):
    model = Surgery
    context_object_name = 'surgeries'
    template_name = 'Manager/surgery_list.html'
    queryset = Surgery.objects.select_related('operating_room').all()

class SurgeryCreateView(LoginRequiredMixin, CreateView):
    model = Surgery
    form_class = SurgeryForm
    template_name = "Manager/surgery_form.html"
    success_url = reverse_lazy('surgery_list')

class SurgeryUpdateView(LoginRequiredMixin, UpdateView):
    model = Surgery
    form_class = SurgeryForm
    template_name = "Manager/surgery_form.html"
    success_url = reverse_lazy('surgery_list')

class SurgeryDeleteView(LoginRequiredMixin, DeleteView):
    model = Surgery
    template_name = "Manager/surgery_confirm_delete.html"
    success_url = reverse_lazy('surgery_list')
