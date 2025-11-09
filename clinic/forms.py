from django import forms
from .models import Specialization, Doctor, Patient, Cabinet, Service, Schedule, Appointment, MedicalRecord

class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите название специальности',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Опишите специальность...',
                'style': 'border-left: 4px solid #28a745; resize: vertical;'
            }),
        }
        labels = {
            'name': 'Название специальности',
            'description': 'Описание специальности',
        }
        help_texts = {
            'name': 'Например: Терапевт, Хирург, Кардиолог',
            'description': 'Подробное описание специальности и обязанностей',
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'first_name', 'last_name', 'middle_name', 'experience', 'phone']
        widgets = {
            'specialization': forms.Select(attrs={
                'class': 'form-select form-select-lg',
                'style': 'border-left: 4px solid #6f42c1;'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя врача',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия врача',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество врача',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'experience': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стаж работы в годах',
                'min': '0',
                'max': '50',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'pattern': '^\\+7 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}$',
                'style': 'border-left: 4px solid #e83e8c;'
            }),
        }
        labels = {
            'specialization': 'Медицинская специальность',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'experience': 'Стаж работы (лет)',
            'phone': 'Контактный телефон',
        }
        help_texts = {
            'phone': 'Формат: +7 (XXX) XXX-XX-XX',
            'experience': 'Укажите количество полных лет работы по специальности',
        }

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'middle_name', 'birth_date', 'phone', 'email', 'address']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пациента',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия пациента',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество пациента',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+7 (XXX) XXX-XX-XX',
                'style': 'border-left: 4px solid #e83e8c;'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'patient@example.com',
                'style': 'border-left: 4px solid #17a2b8;'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Полный адрес проживания...',
                'style': 'border-left: 4px solid #6f42c1; resize: vertical;'
            }),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'birth_date': 'Дата рождения',
            'phone': 'Телефон',
            'email': 'Электронная почта',
            'address': 'Адрес проживания',
        }

class CabinetForm(forms.ModelForm):
    class Meta:
        model = Cabinet
        fields = ['number', 'floor', 'description']
        widgets = {
            'number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 101 или А-12',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'floor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Этаж',
                'min': '1',
                'max': '10',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Опишите назначение кабинета...',
                'style': 'border-left: 4px solid #28a745; resize: vertical;'
            }),
        }
        labels = {
            'number': 'Номер кабинета',
            'floor': 'Этаж',
            'description': 'Описание кабинета',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Название медицинской услуги',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Подробное описание услуги...',
                'style': 'border-left: 4px solid #28a745; resize: vertical;'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0',
                'style': 'border-left: 4px solid #dc3545;'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длительность в минутах',
                'min': '5',
                'max': '480',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
        }
        labels = {
            'name': 'Название услуги',
            'description': 'Описание услуги',
            'price': 'Стоимость (руб.)',
            'duration': 'Длительность (мин.)',
        }
        help_texts = {
            'price': 'Стоимость в рублях',
            'duration': 'Продолжительность услуги в минутах',
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'cabinet', 'date', 'start_time', 'end_time', 'is_available']
        widgets = {
            'doctor': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #6f42c1;'
            }),
            'cabinet': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'style': 'border-left: 4px solid #28a745;'
            }),
            'start_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
            'end_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'style': 'border-left: 4px solid #dc3545;'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'transform: scale(1.2); margin-left: 10px;'
            }),
        }
        labels = {
            'doctor': 'Врач',
            'cabinet': 'Кабинет',
            'date': 'Дата приема',
            'start_time': 'Время начала',
            'end_time': 'Время окончания',
            'is_available': 'Доступно для записи',
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'schedule', 'service', 'appointment_date', 'status', 'notes']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'schedule': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #6f42c1;'
            }),
            'service': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'appointment_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'style': 'border-left: 4px solid #fd7e14;'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #17a2b8;'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительные примечания...',
                'style': 'border-left: 4px solid #e83e8c; resize: vertical;'
            }),
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'appointment', 'diagnosis', 'treatment', 'notes']
        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #20c997;'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #007bff;'
            }),
            'appointment': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-left: 4px solid #6f42c1;'
            }),
            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Подробное описание диагноза...',
                'style': 'border-left: 4px solid #dc3545; resize: vertical;'
            }),
            'treatment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Назначенное лечение и рекомендации...',
                'style': 'border-left: 4px solid #28a745; resize: vertical;'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Дополнительные медицинские заметки...',
                'style': 'border-left: 4px solid #fd7e14; resize: vertical;'
            }),
        }
        labels = {
            'patient': 'Пациент',
            'doctor': 'Лечащий врач',
            'appointment': 'Запись на прием',
            'diagnosis': 'Диагноз',
            'treatment': 'Лечение и рекомендации',
            'notes': 'Дополнительные заметки',
        }