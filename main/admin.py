from django.contrib import admin
from .models import Student, Group, Attendance

# Register your models here.
class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0
    fields = ('date', 'is_present', 'grade')
    readonly_fields = ('date',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'login', 'group')
    search_fields = ('first_name', 'last_name', 'login')
    list_filter = ('group',)
    inlines = [AttendanceInline]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'group', 'date', 'is_present', 'grade')
    list_filter = ('group', 'date', 'is_present')
    search_fields = ('student__first_name', 'student__last_name')