from rest_framework import serializers
from .models import Course,Subject,Lesson



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','course_name']





class SubjectSerializer(serializers.ModelSerializer):
    course=serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    class Meta:
        model=Subject
        fields=['id','course','subject_name']
        
    def to_representation(self, instance):
        return {
            "id":instance.id,
            "course":instance.course.course_name,
            "subject_name":instance.subject_name
        }

   

class LessonSerializer(serializers.ModelSerializer):
    # chapter=serializers.PrimaryKeyRelatedField(queryset=Chapter.objects.all())
    class Meta:
        model=Lesson
        fields=['id','subject','lesson_name','video']