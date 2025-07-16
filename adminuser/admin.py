from django.contrib import admin
from .models import Course
from .models import Course,Subject,Lesson

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Lesson)


