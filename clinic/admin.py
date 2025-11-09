from django.contrib import admin
from .models import *

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'specialization', 'experience']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'birth_date', 'phone']

@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    list_display = ['number', 'floor', 'description']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'duration']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'cabinet', 'date', 'start_time', 'is_available']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'schedule', 'service', 'appointment_date', 'status']

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'record_date', 'diagnosis']