from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.FileField(upload_to='profile-photo')
    login = models.CharField(
        max_length=10, 
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message='Login faqat 10 xonali raqamlardan iborat bo‘lishi kerak.',
                code='invalid_login'
            )
        ],
        unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    pasport = models.CharField(
        max_length=9,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z]{2}\d{7}$',
                message="Pasport raqamingizni to'g'ri kiriting. Masalan: AB1234567"
            )
        ],
        unique=True,)
    email = models.EmailField(max_length=254)
    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message="Telefon raqami +998 bilan boshlanib, jami 13 ta belgidan iborat bo‘lishi kerak (masalan: +998901234567)"
            )
        ],
        unique=True
    )
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='attendances')
    is_present = models.BooleanField(default=False)
    grade = models.PositiveIntegerField(null=True, blank=True)
    date = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.group and self.student:
            self.group = self.student.group
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return self.student.first_name