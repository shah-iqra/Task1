from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name

    def course_count(self):
        return self.courses.count()
    course_count.short_description = "Number of Courses"


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.PositiveIntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.course_code} - {self.title}"

    def enrolled_students_count(self):
        return self.enrollments.count()
    enrolled_students_count.short_description = "Enrolled Students"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
