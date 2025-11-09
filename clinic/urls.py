from django.urls import include, path
from . import views

app_name = 'clinic'

urlpatterns = [
    # Аутентификация
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Списки
    path('specializations/', views.specialization_list, name='specialization_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('patients/', views.patient_list, name='patient_list'),
    path('cabinets/', views.cabinet_list, name='cabinet_list'),
    path('services/', views.service_list, name='service_list'),
    path('schedules/', views.schedule_list, name='schedule_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    
    # Создание
    path('specializations/create/', views.specialization_create, name='specialization_create'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('cabinets/create/', views.cabinet_create, name='cabinet_create'),
    path('services/create/', views.service_create, name='service_create'),
    path('schedules/create/', views.schedule_create, name='schedule_create'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('medical-records/create/', views.medical_record_create, name='medical_record_create'),
    
    # Детальный просмотр
    path('specializations/<int:pk>/', views.specialization_detail, name='specialization_detail'),
    path('doctors/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('patients/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('cabinets/<int:pk>/', views.cabinet_detail, name='cabinet_detail'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('schedules/<int:pk>/', views.schedule_detail, name='schedule_detail'),
    path('appointments/<int:pk>/', views.appointment_detail, name='appointment_detail'),
    path('medical-records/<int:pk>/', views.medical_record_detail, name='medical_record_detail'),
    
    # Редактирование
    path('specializations/<int:pk>/edit/', views.specialization_edit, name='specialization_edit'),
    path('doctors/<int:pk>/edit/', views.doctor_edit, name='doctor_edit'),
    path('patients/<int:pk>/edit/', views.patient_edit, name='patient_edit'),
    path('cabinets/<int:pk>/edit/', views.cabinet_edit, name='cabinet_edit'),
    path('services/<int:pk>/edit/', views.service_edit, name='service_edit'),
    path('schedules/<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('appointments/<int:pk>/edit/', views.appointment_edit, name='appointment_edit'),
    path('medical-records/<int:pk>/edit/', views.medical_record_edit, name='medical_record_edit'),
    
    # Удаление
    path('specializations/<int:pk>/delete/', views.specialization_delete, name='specialization_delete'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    path('cabinets/<int:pk>/delete/', views.cabinet_delete, name='cabinet_delete'),
    path('services/<int:pk>/delete/', views.service_delete, name='service_delete'),
    path('schedules/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),
    path('appointments/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('medical-records/<int:pk>/delete/', views.medical_record_delete, name='medical_record_delete'),

# API
    path('api/', include('clinic.api_urls')),
]