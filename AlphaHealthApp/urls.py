from django.urls import path
from . import views

app_name = 'AlphaHealthApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('PatientLogin/', views.PatientLogin, name = 'PatientLogin'),
    path('PatientLoginPage/', views.PatientLoginPage, name = 'PatientLoginPage'),
    path('NewPatient/', views.NewPatient, name = 'NewPatient'),
    path('PatientUpdate/', views.PatientUpdate, name = 'PatientUpdate'),
    path('CreatePatient/', views.CreatePatient, name = 'CreatePatient'),

    path('CreateAppointment/', views.CreateAppointment, name = 'CreateAppointment'),
    path('ViewAppointment/', views.ViewAppointment, name = 'ViewAppointment'),

    path('DoctorView/', views.DoctorView, name = 'DoctorView'),
    path('ViewAllAppointment/', views.ViewAllAppointment, name = 'ViewAllAppointment'),

]
