from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

# Базовый класс для всех ViewSets с поиском
class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    def get_permissions(self):
        """
        Разграничение прав доступа:
        - GET: любой аутентифицированный пользователь
        - POST, PUT, PATCH, DELETE: только администраторы
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

class SpecializationViewSet(BaseViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    search_fields = ['name']  # Поиск по названию специальности

class DoctorViewSet(BaseViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    search_fields = ['last_name', 'first_name']  # Поиск по фамилии и имени

class PatientViewSet(BaseViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    search_fields = ['last_name', 'first_name']  # Поиск по фамилии и имени
    
    def get_permissions(self):
        """
        Для пациентов ограничиваем:
        - GET: любой аутентифицированный пользователь
        - POST, PUT, PATCH, DELETE: запрещено всем
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated()]  # Запрещаем все остальные методы

class CabinetViewSet(BaseViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    search_fields = ['number']  # Поиск по номеру кабинета

class ServiceViewSet(BaseViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    search_fields = ['name']  # Поиск по названию услуги

class ScheduleViewSet(BaseViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    search_fields = ['doctor__last_name']  # Поиск по фамилии врача

class AppointmentViewSet(BaseViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    search_fields = ['patient__last_name']  # Поиск по фамилии пациента

class MedicalRecordViewSet(BaseViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    search_fields = ['patient__last_name']  # Поиск по фамилии пациента
    
    def get_permissions(self):
        """
        Для медицинских карт ограничиваем:
        - GET: любой аутентифицированный пользователь
        - POST, PUT, PATCH, DELETE: запрещено всем
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAuthenticated()]  # Запрещаем все остальные методы