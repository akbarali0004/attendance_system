# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# from django.core.validators import RegexValidator
# from django.utils import timezone
# from .generate_login import generate_numeric_login
# from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# # Create your models here.
# # class User(AbstractUser):
# #     ROLE_CHOICES = (
# #         ('dean', 'Dekan'),
# #         ('teacher', 'Teacher'),
# #         ('student', 'Student'),
# #     )
# #     role = models.CharField(max_length=20, choices=ROLE_CHOICES)

# #     def __str__(self):
# #         return f"{self.username} ({self.role})"


# # class Group(models.Model):
# #     name = models.CharField(max_length=50)

# #     def __str__(self):
# #         return self.name


# # class Teacher(models.Model):
# #     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# #     first_name = models.CharField(max_length=50)
# #     last_name = models.CharField(max_length=50)
# #     image = models.FileField(upload_to='profile-photo')
# #     login = models.CharField(max_length=12, unique=True, blank=True)
# #     pasport = models.CharField(
# #         max_length=9,
# #         validators=[
# #             RegexValidator(
# #                 regex=r'^[A-Za-z]{2}\d{7}$',
# #                 message="Pasport mal'umtlaringizni to'g'ri kiriting. Masalan: AB1234567"
# #             )
# #         ],
# #         unique=True,)
# #     email = models.EmailField(max_length=254)
# #     phone = models.CharField(
# #         max_length=13,
# #         validators=[
# #             RegexValidator(
# #                 regex=r'^\+998\d{9}$',
# #                 message="Telefon raqami +998 bilan boshlanib, jami 13 ta belgidan iborat bo‘lishi kerak (masalan: +998901234567)"
# #             )
# #         ],
# #         unique=True
# #     )
# #     password = models.CharField(max_length=30)

# #     def __str__(self):
# #         return self.first_name
    
# #     def save(self, *args, **kwargs):
# #         if not self.login:
# #             code = generate_numeric_login()
# #             while Student.objects.filter(login=code).exists():
# #                 code = generate_numeric_login()
# #             self.login = code
# #         super().save(*args, **kwargs)


# class StudentManager(BaseUserManager):
#     def create_user(self, login, password=None, **extra_fields):
#         if not login:
#             raise ValueError("Login field is required")
#         user = self.model(login=login, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, login, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(login, password, **extra_fields)
    

# # class Student(models.Model):
# #     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# #     first_name = models.CharField(max_length=50)
# #     last_name = models.CharField(max_length=50)
# #     image = models.FileField(upload_to='profile-photo')
# #     login = models.CharField(max_length=12, unique=True, blank=True)
# #     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
# #     pasport = models.CharField(
# #         max_length=9,
# #         validators=[
# #             RegexValidator(
# #                 regex=r'^[A-Za-z]{2}\d{7}$',
# #                 message="Pasport raqamingizni to'g'ri kiriting. Masalan: AB1234567"
# #             )
# #         ],
# #         unique=True,)
# #     email = models.EmailField(max_length=254)
# #     phone = models.CharField(
# #         max_length=13,
# #         validators=[
# #             RegexValidator(
# #                 regex=r'^\+998\d{9}$',
# #                 message="Telefon raqami +998 bilan boshlanib, jami 13 ta belgidan iborat bo‘lishi kerak (masalan: +998901234567)"
# #             )
# #         ],
# #         unique=True
# #     )
# #     password = models.CharField(max_length=30)

# #     def __str__(self):
# #         return self.first_name
    
# #     def save(self, *args, **kwargs):
# #         if not self.login:
# #             code = generate_numeric_login()
# #             while Student.objects.filter(login=code).exists():
# #                 code = generate_numeric_login()
# #             self.login = code
# #         super().save(*args, **kwargs)


# class Student(AbstractBaseUser, PermissionsMixin):
#     login = models.CharField(max_length=12, unique=True)
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=254, blank=True, null=True)
#     image = models.FileField(upload_to='profile-photo', blank=True, null=True)
#     pasport = models.CharField(
#         max_length=9,
#         validators=[
#             RegexValidator(
#                 regex=r'^[A-Za-z]{2}\d{7}$',
#                 message="Pasport raqamingizni to'g'ri kiriting. Masalan: AB1234567"
#             )
#         ],
#         unique=True,
#         blank=True, null=True
#     )
#     phone = models.CharField(
#         max_length=13,
#         validators=[
#             RegexValidator(
#                 regex=r'^\+998\d{9}$',
#                 message="Telefon raqami +998 bilan boshlanib, jami 13 ta belgidan iborat bo‘lishi kerak (masalan: +998901234567)"
#             )
#         ],
#         unique=True,
#         blank=True, null=True
#     )
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='students', blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(default=timezone.now)

#     objects = StudentManager()

#     USERNAME_FIELD = 'login'
#     REQUIRED_FIELDS = ['full_name']

#     def __str__(self):
#         return self.login


# # class Attendance(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
# #     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='attendances')
# #     is_present = models.BooleanField(default=False)
# #     grade = models.PositiveIntegerField(null=True, blank=True)
# #     date = models.DateField(default=timezone.now)

# #     def save(self, *args, **kwargs):
# #         if not self.group and self.student:
# #             self.group = self.student.group
# #         super().save(*args, **kwargs)

# #     class Meta:
# #         unique_together = ('student', 'date')

# #     def __str__(self):
# #         return self.student.first_name