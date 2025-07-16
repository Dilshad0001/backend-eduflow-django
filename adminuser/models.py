from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.course_name
    


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.subject_name} ({self.course.course_name})"



class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)  
    lesson_name = models.CharField(max_length=30)
    video = models.FileField(upload_to='videos/', null=True, blank=True) 