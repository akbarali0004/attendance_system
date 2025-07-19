from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Group, Attendance
from django.utils import timezone

# Create your views here.
def home(request):
    groups = Group.objects.all()
    return render(request, 'home.html', context={'groups':groups})


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = group.students.all()

    if request.method == 'POST':
        for student in students:
            grade_key = f'grade_{student.id}'
            present_key = f'present_{student.id}'

            grade = request.POST.get(grade_key) or None
            is_present = present_key in request.POST  # checkbox borligini tekshiradi

            # Bu yerda saqlash logikasi bo‘ladi
            # print(f"Student: {student.id}, Baho: {grade}, Kelgan: {is_present}")
            # print(request.POST)

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