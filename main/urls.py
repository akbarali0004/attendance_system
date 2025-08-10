from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('dean/', dean_home, name='dean_home'),
    path('teacher/', teacher_home, name='teacher_home'),
    path('student/', student_home, name='student_home'),
    path('logout/', logout_view, name='logout'),
    path('attendance/<int:pk>', group_attendance, name='group_attendance'),
]
