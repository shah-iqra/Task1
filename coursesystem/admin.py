from django.contrib import admin
from .models import Student, Instructor, Course, Enrollment

# Inline for assigning multiple students to a course
class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'enrollment_date')
    search_fields = ('name',)
    list_filter = ('department',)


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'hire_date', 'course_count')
    search_fields = ('name', 'email')
    list_filter = ('department',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'title', 'credits', 'instructor', 'enrolled_students_count')
    search_fields = ('course_code', 'title', 'instructor__name')
    list_filter = ('credits', 'instructor')
    inlines = [EnrollmentInline]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enrollment_date', 'grade')
    search_fields = ('student__name', 'course__title')
    list_filter = ('enrollment_date', 'grade')
