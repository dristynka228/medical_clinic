from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название специальности")
    description = models.TextField(verbose_name="Описание", blank=True)
    
    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, verbose_name="Специальность")
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    experience = models.IntegerField(verbose_name="Стаж (лет)")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    
    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

class Patient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество", blank=True)
    birth_date = models.DateField(verbose_name="Дата рождения")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email", blank=True)
    address = models.TextField(verbose_name="Адрес", blank=True)
    
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

# Добавляем после существующих моделей в clinic/models.py

class Cabinet(models.Model):
    number = models.CharField(max_length=10, verbose_name="Номер кабинета")
    floor = models.IntegerField(verbose_name="Этаж")
    description = models.TextField(verbose_name="Описание", blank=True)
    
    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"
    
    def __str__(self):
        return f"Кабинет {self.number}"

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    duration = models.IntegerField(verbose_name="Длительность (минут)")
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
    
    def __str__(self):
        return self.name

class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name="Кабинет")
    date = models.DateField(verbose_name="Дата приема")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    is_available = models.BooleanField(default=True, verbose_name="Доступно для записи")
    
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"
    
    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time}"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Запланирован'),
        ('completed', 'Завершен'),
        ('cancelled', 'Отменен'),
        ('no_show', 'Не явился'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name="Расписание")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга")
    appointment_date = models.DateTimeField(verbose_name="Дата и время записи")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled', verbose_name="Статус")
    notes = models.TextField(verbose_name="Примечания", blank=True)
    
    class Meta:
        verbose_name = "Запись на прием"
        verbose_name_plural = "Записи на прием"
    
    def __str__(self):
        return f"{self.patient} - {self.appointment_date}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, verbose_name="Запись на прием")
    diagnosis = models.TextField(verbose_name="Диагноз")
    treatment = models.TextField(verbose_name="Лечение", blank=True)
    record_date = models.DateField(auto_now_add=True, verbose_name="Дата записи")
    notes = models.TextField(verbose_name="Заметки", blank=True)
    
    class Meta:
        verbose_name = "Медицинская карта"
        verbose_name_plural = "Медицинские карты"
    
    def __str__(self):
        return f"Карта {self.patient} - {self.record_date}"
    