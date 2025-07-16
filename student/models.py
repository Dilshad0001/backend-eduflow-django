from django.db import models
from account .models import CustomUser
from adminuser.models import Course

class StudentProfile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=12)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    


class AssignmentTask(models.Model):
    students = models.ManyToManyField(StudentProfile,related_name="assigned_tasks")
    task_name=models.CharField(max_length=50)
    task_file=models.FileField(upload_to='assignment/', null=True, blank=True) 
    description=models.TextField(null=True)
    uploaded_at=models.DateField(auto_now_add=True)
    submission_deadline=models.DateTimeField(null=True)
    is_completed=models.BooleanField(default=False)
    

    def __str__(self):
        return self.task_name    
    


class AssignmentSubmission(models.Model):
    STATUS_CHOICES=[
        ("pending","pending"),
        ("submitted","submitted"),
        ("approved","approved"),
        ("rejected","rejected")
    ]
    student=models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    assignment = models.ForeignKey(AssignmentTask, on_delete=models.CASCADE)
    file=models.FileField(upload_to="submissions/",null=True)
    submitted_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES,default="pending")
    mark=models.PositiveBigIntegerField(null=True,blank=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.full_name}-{self.assignment.task_name}"
    
class Leaderboard(models.Model):
    student_name=models.OneToOneField(StudentProfile, on_delete=models.CASCADE)
    mark=models.FloatField(null=True)

    def __str__(self):
        return f"{self.student_name} with mark{self.mark} "    