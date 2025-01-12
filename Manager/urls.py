from django.urls import path
from django.contrib.auth import views as auth_views
from Manager.views import (IndexView, DoctorListView, PatientListView,
                           PatientCreateView, PatientUpdateView, PatientDeleteView,
                           SurgeryListView, SurgeryCreateView,
                           SurgeryUpdateView, SurgeryDeleteView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('patients/new/', PatientCreateView.as_view(), name='patient_create'),
    path('login/', auth_views.LoginView.as_view(template_name='Manager/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('patients/edit/<int:pk>/', PatientUpdateView.as_view(), name='patient_update'),
    path('patients/delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('surgeries/', SurgeryListView.as_view(), name='surgery_list'),
    path('surgeries/new/', SurgeryCreateView.as_view(), name='surgery_create'),
    path('surgeries/edit/<int:pk>/', SurgeryUpdateView.as_view(), name='surgery_update'),
    path('surgeries/delete/<int:pk>/', SurgeryDeleteView.as_view(), name='surgery_delete'),
]
