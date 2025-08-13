from .models import Teacher, Student

def user_context(request):
    login = request.session.get('login')
    role = request.session.get('role')
    
    user = None
    if role in ['assistent', 'senior', 'docent', 'professor', 'head_of_department', 'dean']:
        user = Teacher.objects.filter(login=login).first()
    elif role == 'student':
        user = Student.objects.filter(login=login).first()
    
    return {'user': user}
