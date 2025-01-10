from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, doctor_list

urlpatterns = [
    path('', index, name='index'),
    path('doctors/', doctor_list, name='doctor_list'),
    path('login/', auth_views.LoginView.as_view(template_name='Manager/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
