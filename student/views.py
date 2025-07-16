# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import StudentProfile,AssignmentTask,AssignmentSubmission,Leaderboard
# from rest_framework import status
# from .serializers import StudentProfileSerializer,TaskSerializer,AssignmentSubmissionSerializer,LeaderBoardSerializer,studentSubmissionSerializer
# from rest_framework.permissions import IsAuthenticated,AllowAny
# from adminuser.models import Course,Subject,Lesson
# from adminuser.serializers import CourseSerializer,SubjectSerializer,LessonSerializer
# from django.db.models import Q


# class StudentprofileStudentView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         try:
#             profile_data=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"no user found"},status=status.HTTP_204_NO_CONTENT)
#         ser= StudentProfileSerializer(profile_data)
#         return Response(ser.data)
#     def post(self, request):
#         new_data=request.data
#         print("new course===",new_data)
#         new_data['user']=request.user.id
#         ser = StudentProfileSerializer(data=new_data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#     def patch(self,request):
#         new_d=request.data
#         print('new course===',new_d)

#         try:
#             profile_instance=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"no profilr found"},status=status.HTTP_204_NO_CONTENT)
#         ser=StudentProfileSerializer(profile_instance,data=request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
# \


# class StudentCourseView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get (self,request):
#         courses=Course.objects.all()
#         print("courses===============================",courses)
#         ser=CourseSerializer(courses,many=True)
#         return Response(ser.data)
    

# class StudentSubjectView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         try:
#             student_profile=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT)
#         student_course=student_profile.course 
#         if student_course is None:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT)
#         subjects=Subject.objects.filter(course=student_course)
#         ser=SubjectSerializer(subjects,many=True)
#         return Response(ser.data)
    

# class StudentLessonView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         try:
#             student_profile=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT)
#         student_course=student_profile.course 
#         subject_id=request.GET.get('subjectId')
#         lesson_id=request.GET.get('lessonId')
#         print('====',subject_id)
#         if student_course is None:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT)
#         if subject_id:
#             k=Lesson.objects.filter(Q(subject__course__course_name=student_course) & Q(subject=subject_id))
#             ser=LessonSerializer(k,many=True)
#             print("lesoo==subjec==",ser.data)
#             return Response(ser.data)
#         elif lesson_id:
#             k=Lesson.objects.get(id=lesson_id)
#             ser=LessonSerializer(k)
#             return Response(ser.data)
#         lessons=Lesson.objects.filter(subject__course=student_course)
#         ser=LessonSerializer(lessons,many=True)
#         return Response(ser.data)



# class StudentTaskView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         try:
#             student=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT) 
#         tasks_assigned=AssignmentTask.objects.filter(students=student).values_list("id",flat=True)
#         submitted_task_ids = AssignmentSubmission.objects.filter(student=student).values_list("assignment", flat=True)
#         task_ids = tasks_assigned.exclude(id__in=submitted_task_ids)
#         k=AssignmentTask.objects.filter(id__in=task_ids)
#         ser=TaskSerializer(k,many=True)
#         return Response(ser.data)
    
   


# class StudentSubmissionView(APIView):
#     permission_classes=[IsAuthenticated]
#     def get(self,request):
#         not_complted=request.GET.get('notCompleted')
            
#         try:
#             student=StudentProfile.objects.get(user=request.user)
#         except:
#             return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT) 
#         submition=AssignmentSubmission.objects.filter(student=student)
#         if not_complted:
#             submition = AssignmentSubmission.objects.filter(student=student, is_completed=False)
#         ser=AssignmentSubmissionSerializer(submition,many=True)
#         return Response(ser.data)
#     # def post(self,request):
#     #     new_submission=request.data
#     #     try:
#     #         student=StudentProfile.objects.get(user=request.user)
#     #     except:
#     #         return Response({"message":"complete profile"},status=status.HTTP_204_NO_CONTENT) 
#     #     new_submission['student']=student.id
#     #     new_submission['status']='submitted'
#     #     ser=AssignmentSubmissionSerializer(data=new_submission)
#     #     if ser.is_valid():
#     #         ser.save()
#     #         return Response(ser.data)
#         # return Response(ser.errors)
#     def patch(self,request):
#         submission_id=request.GET.get('submissionId')
#         if not submission_id:
#             return Response("submission id is requierd")
#         ins = AssignmentSubmission.objects.get(id=submission_id)
#         if ins.student.user != request.user:
#             return Response({"detail": "Unauthorized access."}, status=403)
#         ser=studentSubmissionSerializer(ins,request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)



# class LeaderBoardStudentView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         leaderboard = Leaderboard.objects.all().order_by('-mark')
#         ser = LeaderBoardSerializer(leaderboard, many=True)

#         # Find current student
#         try:
#             student_profile = StudentProfile.objects.get(user=request.user)
#             leaderboard_list = list(leaderboard)
#             my_rank = None
#             my_mark = None
#             my_name = student_profile.full_name

#             for idx, entry in enumerate(leaderboard_list):
#                 if entry.student_name == student_profile:
#                     my_rank = idx + 1
#                     my_mark = entry.mark
#                     break

#         except StudentProfile.DoesNotExist:
#             my_rank = None
#             my_mark = None
#             my_name = None

#         return Response({
#             "leaderboard": ser.data,
#             "my_mark": my_mark,
#             "my_rank": my_rank,
#             "my_name": my_name,
#         })








from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import StudentProfile, AssignmentTask, AssignmentSubmission, Leaderboard
from rest_framework import status
from .serializers import StudentProfileSerializer, TaskSerializer, AssignmentSubmissionSerializer, LeaderBoardSerializer, studentSubmissionSerializer
from rest_framework.permissions import IsAuthenticated
from adminuser.models import Course, Subject, Lesson
from adminuser.serializers import CourseSerializer, SubjectSerializer, LessonSerializer
from django.db.models import Q


class StudentprofileStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile_data = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "No user found"}, status=status.HTTP_404_NOT_FOUND)
        ser = StudentProfileSerializer(profile_data)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        new_data = request.data
        new_data['user'] = request.user.id
        ser = StudentProfileSerializer(data=new_data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            profile_instance = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "No profile found"}, status=status.HTTP_404_NOT_FOUND)
        ser = StudentProfileSerializer(profile_instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentCourseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        courses = Course.objects.all()
        ser = CourseSerializer(courses, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class StudentSubjectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student_profile = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "Complete profile"}, status=status.HTTP_404_NOT_FOUND)

        student_course = student_profile.course
        if not student_course:
            return Response({"message": "Complete profile"}, status=status.HTTP_400_BAD_REQUEST)

        subjects = Subject.objects.filter(course=student_course)
        ser = SubjectSerializer(subjects, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class StudentLessonView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student_profile = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "Complete profile"}, status=status.HTTP_404_NOT_FOUND)

        student_course = student_profile.course
        subject_id = request.GET.get('subjectId')
        lesson_id = request.GET.get('lessonId')

        if not student_course:
            return Response({"message": "Complete profile"}, status=status.HTTP_400_BAD_REQUEST)

        if subject_id:
            lessons = Lesson.objects.filter(Q(subject__course=student_course) & Q(subject=subject_id))
            ser = LessonSerializer(lessons, many=True)
            return Response(ser.data, status=status.HTTP_200_OK)

        if lesson_id:
            try:
                lesson = Lesson.objects.get(id=lesson_id)
            except Lesson.DoesNotExist:
                return Response({"message": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)
            ser = LessonSerializer(lesson)
            return Response(ser.data, status=status.HTTP_200_OK)

        lessons = Lesson.objects.filter(subject__course=student_course)
        ser = LessonSerializer(lessons, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class StudentTaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "Complete profile"}, status=status.HTTP_404_NOT_FOUND)

        tasks_assigned = AssignmentTask.objects.filter(students=student).values_list("id", flat=True)
        submitted_task_ids = AssignmentSubmission.objects.filter(student=student).values_list("assignment", flat=True)
        task_ids = tasks_assigned.exclude(id__in=submitted_task_ids)
        tasks = AssignmentTask.objects.filter(id__in=task_ids)
        ser = TaskSerializer(tasks, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class StudentSubmissionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        not_completed = request.GET.get('notCompleted')
        try:
            student = StudentProfile.objects.get(user=request.user)
        except StudentProfile.DoesNotExist:
            return Response({"message": "Complete profile"}, status=status.HTTP_404_NOT_FOUND)

        submissions = AssignmentSubmission.objects.filter(student=student)
        if not_completed:
            submissions = submissions.filter(is_completed=False)


        ser = AssignmentSubmissionSerializer(submissions, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def patch(self, request):
        submission_id = request.GET.get('submissionId')
        if not submission_id:
            return Response({"message": "Submission ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = AssignmentSubmission.objects.get(id=submission_id)
        except AssignmentSubmission.DoesNotExist:
            return Response({"message": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)

        if instance.student.user != request.user:
            return Response({"detail": "Unauthorized access."}, status=status.HTTP_403_FORBIDDEN)

        ser = studentSubmissionSerializer(instance, request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class LeaderBoardStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        leaderboard = Leaderboard.objects.all().order_by('-mark')
        ser = LeaderBoardSerializer(leaderboard, many=True)

        my_rank = None
        my_mark = None
        my_name = None

        try:
            student_profile = StudentProfile.objects.get(user=request.user)
            leaderboard_list = list(leaderboard)

            for idx, entry in enumerate(leaderboard_list):
                if entry.student_name == student_profile:
                    my_rank = idx + 1
                    my_mark = entry.mark
                    my_name = student_profile.full_name
                    break
        except StudentProfile.DoesNotExist:
            pass

        return Response({
            "leaderboard": ser.data,
            "my_mark": my_mark,
            "my_rank": my_rank,
            "my_name": my_name,
        }, status=status.HTTP_200_OK)
