from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.urls import reverse_lazy
from .models import Teacher, Student, Group, Attendance
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.cache import never_cache




def session_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


# Create your views here.
@session_login_required
def home(request):
    role = request.session.get('role')
    if role == 'dean':
        return redirect('dean_home')
    elif role in ['assistent', 'senior', 'docent', 'professor', 'head_of_department']:
        return redirect('teacher_home')
    elif role == 'student':
        return redirect('student_home')
    return redirect('login')


def dean_home(request):
    role = request.session.get('role')
    if role != "dean":
        return redirect('login')
    return render(request, 'home_page/hm.html', context={'page':'Dekan Page'})


def teacher_home(request):
    role = request.session.get('role')
    if role != "teacher":
        return redirect('login')
    return render(request, 'home_page/hm.html', context={'page':"O'qituvchi Page"})


def student_home(request):
    role = request.session.get('role')
    if role != "student":
        return redirect('login')
    return render(request, 'home_page/hm.html', context={'page':'Student Page'})


@never_cache
def login_view(request):
    if request.session.get('user_id'):
        role = request.session.get('role')
        if role == 'student':
            return redirect('student_home')
        elif role == 'dean':
            return redirect('dean_home')
        elif role in ['assistent', 'senior', 'docent', 'professor', 'head_of_department']:
            return redirect('teacher_home')

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        user = None
        role = None

        # Avval Teacher modelidan qidiramiz
        try:
            user = Teacher.objects.get(login=login)
            role = user.position
            user_type = 'teacher'
        except Teacher.DoesNotExist:
            # Keyin Student modelidan qidiramiz
            try:
                user = Student.objects.get(login=login)
                role = 'student'
                user_type = 'student'
            except Student.DoesNotExist:
                messages.error(request, "Login topilmadi.")
                return redirect('login')

        # Agar login topilgan bo‘lsa, parolni tekshiramiz
        if check_password(password, user.password):
            request.session['user_id'] = user.id
            request.session['role'] = role

            # Remember me
            if remember_me:
                request.session.set_expiry(172800)  # 2 kun
            else:
                request.session.set_expiry(0)

            messages.success(request, "✅ Tizimga muvaffaqiyatli kirdingiz.")

            # Lavozimga qarab yo‘naltirish
            if role == 'student':
                return redirect('student_home')
            elif role == 'dean':
                return redirect('dean_home')
            elif role in ['assistent', 'senior', 'docent', 'professor', 'head_of_department']:
                return redirect('teacher_home')
        else:
            messages.error(request, "Parol xato.")
            return redirect('login')

    return render(request, 'registration/login.html')



def logout_view(request):
    request.session.flush()
    messages.error(request, "🔒 Tizimdan muvaffaqiyatli chiqdingiz.")
    return redirect('login')


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = group.students.all()

    if request.method == 'POST':
        for student in students:
            grade_key = f'grade_{student.id}'
            present_key = f'present_{student.id}'

            grade = request.POST.get(grade_key) or None
            is_present = present_key in request.POST  # checkbox borligini tekshiradi

            Attendance.objects.update_or_create(
                student=student,
                date=timezone.now().date(),
                defaults={
                    'group': group,
                    'is_present': is_present,
                    'grade': grade
                }
            )
        return redirect('home')

    attendance_data = Attendance.objects.filter(group=group, date=timezone.now().date())
    attendance_dict = {str(a.student_id): a for a in attendance_data}
    return render(request, 'group_detail.html', context={'group': group, 'students':students, 'attendance_dict': attendance_dict})