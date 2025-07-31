from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator
from django.utils import timezone
from .generate_login import generate_numeric_login



# class Subject(models.Model):
#     name = models.CharField(max_length=50)


class BaseProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=[('male', 'Erkak'), ('female', 'Ayol')])
    image = models.FileField(upload_to='profile-photo', blank=True, null=True)
    password = models.CharField(max_length=30)
    login = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message="Login faqat 12 ta raqamdan iborat bo'lishi kerak."
            )
        ]
    )
    pasport = models.CharField(
        max_length=9,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z]{2}\d{7}$',
                message="Pasport ma'lumotlari xato kiritildi. (N: AD1234567)"
            )
        ],)
    email = models.EmailField(max_length=254)
    phone = models.CharField(
        max_length=13,
        validators=[
            RegexValidator(
                regex=r'^\+998\d{9}$',
                message="Telefon raqami xato kiritildi. (N: +998901234567)"
            )
        ],
        unique=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.first_name
    
    def save(self, *args, **kwargs):
        if not self.login:
            code = generate_numeric_login()
            while Student.objects.filter(login=code).exists() or Teacher.objects.filter(login=code).exists():
                code = generate_numeric_login()
            self.login = code
        
        self.password = make_password(self.password)
        super().save(*args, **kwargs)



class Teacher(BaseProfile):
    # subjects = models.ManyToManyField(Subject)
    POSITIONS = [
        ('assistent', "O'qituvchi"),
        ('senior', "Katta o'qituvchi"),
        ('docent', "Dotsent (PhD)"),
        ('professor', 'Professor'),
        ('head_of_department', 'Kafedra mudiri'),
        ('dean', 'Fakultet dekani'),
    ]
    position = models.CharField(max_length=100, choices=POSITIONS)


class Group(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Student(BaseProfile):
    EDU_TYPES = [
        ('grant', 'Davlat granti asosida'),
        ('contract', 'To‘lov-kontrakt asosida'),
    ]
    edu_type = models.CharField(max_length=12, choices=EDU_TYPES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='students')


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