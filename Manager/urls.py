# Manager/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ... существующие маршруты ...
    path('', views.index, name='index'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('login/', auth_views.LoginView.as_view(template_name='Manager/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
path('patients/edit/<int:pk>/', views.patient_update, name='patient_update'),
path('patients/delete/<int:pk>/', views.patient_delete, name='patient_delete'),
path('surgeries/', views.surgery_list, name='surgery_list'),
path('surgeries/new/', views.surgery_create, name='surgery_create'),
path('surgeries/edit/<int:pk>/', views.surgery_update, name='surgery_update'),
path('surgeries/delete/<int:pk>/', views.surgery_delete, name='surgery_delete'),


]
