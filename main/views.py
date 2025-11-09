from django.shortcuts import render
from clinic.models import *

def home(request):
    from django.utils import timezone
    
    context = {
        # Статистика для карточек
        'doctors_count': Doctor.objects.count(),
        'patients_count': Patient.objects.count(),
        'services_count': Service.objects.count(),
        'cabinets_count': Cabinet.objects.count(),
        'schedules_count': Schedule.objects.count(),
        'appointments_count': Appointment.objects.count(),
        'appointments_today': Appointment.objects.filter(
            appointment_date__date=timezone.now().date()
        ).count(),
        'specializations_count': Specialization.objects.count(),
        'medical_records_count': MedicalRecord.objects.count(),
    }
    return render(request, 'main/home.html', context)