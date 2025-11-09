from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .auth_forms import CustomUserCreationForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'clinic/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')
                return redirect('home')
            else:
                messages.error(request, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()
    
    return render(request, 'clinic/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('home')

def specialization_list(request):
    specializations = Specialization.objects.all()
    return render(request, 'clinic/specialization_list.html', {
        'specializations': specializations
    })

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'clinic/doctor_list.html', {
        'doctors': doctors
    })

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'clinic/patient_list.html', {
        'patients': patients
    })

def cabinet_list(request):
    cabinets = Cabinet.objects.all()
    return render(request, 'clinic/cabinet_list.html', {
        'cabinets': cabinets
    })

def service_list(request):
    services = Service.objects.all()
    return render(request, 'clinic/service_list.html', {
        'services': services
    })

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'clinic/schedule_list.html', {
        'schedules': schedules
    })

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'clinic/appointment_list.html', {
        'appointments': appointments
    })

def medical_record_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'clinic/medical_record_list.html', {
        'medical_records': medical_records
    })

# ===== ФУНКЦИИ СОЗДАНИЯ =====
def specialization_create(request):
    if request.method == 'POST':
        form = SpecializationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Специальность успешно создана!')
            return redirect('clinic:specialization_list')
    else:
        form = SpecializationForm()
    
    return render(request, 'clinic/specialization_form.html', {
        'form': form,
        'title': 'Добавление специальности',
        'action_url': 'clinic:specialization_create'
    })

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Врач успешно добавлен!')
            return redirect('clinic:doctor_list')
    else:
        form = DoctorForm()
    
    return render(request, 'clinic/doctor_form.html', {
        'form': form,
        'title': 'Добавление врача',
        'action_url': 'clinic:doctor_create'
    })

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пациент успешно добавлен!')
            return redirect('clinic:patient_list')
    else:
        form = PatientForm()
    
    return render(request, 'clinic/patient_form.html', {
        'form': form,
        'title': 'Добавление пациента',
        'action_url': 'clinic:patient_create'
    })

def cabinet_create(request):
    if request.method == 'POST':
        form = CabinetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Кабинет успешно добавлен!')
            return redirect('clinic:cabinet_list')
    else:
        form = CabinetForm()
    
    return render(request, 'clinic/cabinet_form.html', {
        'form': form,
        'title': 'Добавление кабинета',
        'action_url': 'clinic:cabinet_create'
    })

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Услуга успешно добавлена!')
            return redirect('clinic:service_list')
    else:
        form = ServiceForm()
    
    return render(request, 'clinic/service_form.html', {
        'form': form,
        'title': 'Добавление услуги',
        'action_url': 'clinic:service_create'
    })

def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Расписание успешно добавлено!')
            return redirect('clinic:schedule_list')
    else:
        form = ScheduleForm()
    
    return render(request, 'clinic/schedule_form.html', {
        'form': form,
        'title': 'Добавление расписания',
        'action_url': 'clinic:schedule_create'
    })

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись на прием успешно создана!')
            return redirect('clinic:appointment_list')
    else:
        form = AppointmentForm()
    
    return render(request, 'clinic/appointment_form.html', {
        'form': form,
        'title': 'Создание записи на прием',
        'action_url': 'clinic:appointment_create'
    })

def medical_record_create(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Медицинская карта успешно создана!')
            return redirect('clinic:medical_record_list')
    else:
        form = MedicalRecordForm()
    
    return render(request, 'clinic/medical_record_form.html', {
        'form': form,
        'title': 'Создание медицинской карты',
        'action_url': 'clinic:medical_record_create'
    })

# ===== ФУНКЦИИ ДЕТАЛЬНОГО ПРОСМОТРА =====
def specialization_detail(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    return render(request, 'clinic/specialization_detail.html', {
        'specialization': specialization
    })

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'clinic/doctor_detail.html', {
        'doctor': doctor
    })

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'clinic/patient_detail.html', {
        'patient': patient
    })

def cabinet_detail(request, pk):
    cabinet = get_object_or_404(Cabinet, pk=pk)
    return render(request, 'clinic/cabinet_detail.html', {
        'cabinet': cabinet
    })

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'clinic/service_detail.html', {
        'service': service
    })

def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'clinic/schedule_detail.html', {
        'schedule': schedule
    })

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'clinic/appointment_detail.html', {
        'appointment': appointment
    })

def medical_record_detail(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    return render(request, 'clinic/medical_record_detail.html', {
        'medical_record': medical_record
    })

# ===== ФУНКЦИИ РЕДАКТИРОВАНИЯ =====
def specialization_edit(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    
    if request.method == 'POST':
        form = SpecializationForm(request.POST, instance=specialization)
        if form.is_valid():
            form.save()
            messages.success(request, 'Специальность успешно обновлена!')
            return redirect('clinic:specialization_detail', pk=specialization.pk)
    else:
        form = SpecializationForm(instance=specialization)
    
    return render(request, 'clinic/specialization_form.html', {
        'form': form,
        'title': f'Редактирование: {specialization.name}',
        'action_url': 'clinic:specialization_edit',
        'object': specialization
    })

def doctor_edit(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные врача успешно обновлены!')
            return redirect('clinic:doctor_detail', pk=doctor.pk)
    else:
        form = DoctorForm(instance=doctor)
    
    return render(request, 'clinic/doctor_form.html', {
        'form': form,
        'title': f'Редактирование: {doctor}',
        'action_url': 'clinic:doctor_edit',
        'object': doctor
    })

def patient_edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные пациента успешно обновлены!')
            return redirect('clinic:patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'clinic/patient_form.html', {
        'form': form,
        'title': f'Редактирование: {patient}',
        'action_url': 'clinic:patient_edit',
        'object': patient
    })

def cabinet_edit(request, pk):
    cabinet = get_object_or_404(Cabinet, pk=pk)
    
    if request.method == 'POST':
        form = CabinetForm(request.POST, instance=cabinet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные кабинета успешно обновлены!')
            return redirect('clinic:cabinet_detail', pk=cabinet.pk)
    else:
        form = CabinetForm(instance=cabinet)
    
    return render(request, 'clinic/cabinet_form.html', {
        'form': form,
        'title': f'Редактирование: {cabinet}',
        'action_url': 'clinic:cabinet_edit',
        'object': cabinet
    })

def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные услуги успешно обновлены!')
            return redirect('clinic:service_detail', pk=service.pk)
    else:
        form = ServiceForm(instance=service)
    
    return render(request, 'clinic/service_form.html', {
        'form': form,
        'title': f'Редактирование: {service.name}',
        'action_url': 'clinic:service_edit',
        'object': service
    })

def schedule_edit(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, 'Расписание успешно обновлено!')
            return redirect('clinic:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm(instance=schedule)
    
    return render(request, 'clinic/schedule_form.html', {
        'form': form,
        'title': f'Редактирование расписания',
        'action_url': 'clinic:schedule_edit',
        'object': schedule
    })

def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись на прием успешно обновлена!')
            return redirect('clinic:appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    
    return render(request, 'clinic/appointment_form.html', {
        'form': form,
        'title': f'Редактирование записи',
        'action_url': 'clinic:appointment_edit',
        'object': appointment
    })

def medical_record_edit(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Медицинская карта успешно обновлена!')
            return redirect('clinic:medical_record_detail', pk=medical_record.pk)
    else:
        form = MedicalRecordForm(instance=medical_record)
    
    return render(request, 'clinic/medical_record_form.html', {
        'form': form,
        'title': f'Редактирование медицинской карты',
        'action_url': 'clinic:medical_record_edit',
        'object': medical_record
    })

# ===== ФУНКЦИИ УДАЛЕНИЯ =====
def specialization_delete(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    
    if request.method == 'POST':
        specialization.delete()
        messages.success(request, 'Специальность успешно удалена!')
        return redirect('clinic:specialization_list')
    
    return render(request, 'clinic/specialization_confirm_delete.html', {
        'specialization': specialization
    })

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Врач успешно удален!')
        return redirect('clinic:doctor_list')
    
    return render(request, 'clinic/doctor_confirm_delete.html', {
        'doctor': doctor
    })

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Пациент успешно удален!')
        return redirect('clinic:patient_list')
    
    return render(request, 'clinic/patient_confirm_delete.html', {
        'patient': patient
    })

def cabinet_delete(request, pk):
    cabinet = get_object_or_404(Cabinet, pk=pk)
    
    if request.method == 'POST':
        cabinet.delete()
        messages.success(request, 'Кабинет успешно удален!')
        return redirect('clinic:cabinet_list')
    
    return render(request, 'clinic/cabinet_confirm_delete.html', {
        'cabinet': cabinet
    })

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Услуга успешно удалена!')
        return redirect('clinic:service_list')
    
    return render(request, 'clinic/service_confirm_delete.html', {
        'service': service
    })

def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, 'Расписание успешно удалено!')
        return redirect('clinic:schedule_list')
    
    return render(request, 'clinic/schedule_confirm_delete.html', {
        'schedule': schedule
    })

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Запись на прием успешно удалена!')
        return redirect('clinic:appointment_list')
    
    return render(request, 'clinic/appointment_confirm_delete.html', {
        'appointment': appointment
    })

def medical_record_delete(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    
    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, 'Медицинская карта успешно удалена!')
        return redirect('clinic:medical_record_list')
    
    return render(request, 'clinic/medical_record_confirm_delete.html', {
        'medical_record': medical_record
    })  
