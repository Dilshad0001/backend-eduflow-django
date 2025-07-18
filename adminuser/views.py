# from django.shortcuts import render
# from rest_framework.views import APIView
# from account.models import CustomUser
# from account.serializers import CustomUserSerializer
# from rest_framework.response import Response
# from rest_framework.permissions import IsAdminUser
# from django.db.models import Q
# from student.models import StudentProfile,AssignmentTask,AssignmentSubmission,Leaderboard
# from student.serializers import StudentProfileSerializer,AssignmentSubmissionSerializer,TaskSerializer,LeaderBoardSerializer
# from .models import Course,Subject,Lesson
# from .serializers import CourseSerializer,SubjectSerializer,LessonSerializer
# from rest_framework import status



# class UsersListAdminView(APIView):
#     permission_classes=[IsAdminUser]
#     def get (self,request):
#         user_keyword=request.GET.get('user')
#         if user_keyword:
#             users=CustomUser.objects.filter(email__istartswith=user_keyword)
#         else:    
#             users=CustomUser.objects.all()
#         ser=CustomUserSerializer(users,many=True)
#         return Response(ser.data) 
#     def patch(self,request):
#         user_id=request.data['id']
#         try:
#             user=CustomUser.objects.get(id=user_id)
#         except:
#             return Response({"message":"user id is requierd"},status=status.HTTP_204_NO_CONTENT)    
#         ser=CustomUserSerializer(user,request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)        

    


# class StudentListAdminView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         student_keyword = request.GET.get("student")
#         course_keyword = request.GET.get("course")

#         print("course==", course_keyword)

#         queryset = StudentProfile.objects.all()

#         if student_keyword:
#             queryset = queryset.filter(full_name__icontains=student_keyword)

#         if course_keyword:
#             queryset = queryset.filter(course_id=course_keyword)

#         serializer = StudentProfileSerializer(queryset, many=True)
#         return Response(serializer.data)

    
# class AdminCourseView(APIView):
#     permission_classes=[IsAdminUser]
#     def get(self,request):
#         course=Course.objects.all()
#         ser=CourseSerializer(course,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         new_course=request.data
#         ser=CourseSerializer(data=new_course)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def patch(self,request):
#         selected_course=Course.objects.get(id=request.GET.get('courseId'))
#         ser=CourseSerializer(selected_course,data=request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def delete(self,request):
#         selected_course=Course.objects.get(id=request.GET.get('courseId'))
#         selected_course.delete()
#         return Response({"messages":"course deleted"})    


# class AdminSubjectView(APIView):
#     permission_classes=[IsAdminUser]
#     def get(self,request):
#         course_id=request.GET.get('courseId')
#         if course_id:
#             subject=Subject.objects.filter(course=course_id)
#         else:    
#             subject=Subject.objects.all()
#         ser=SubjectSerializer(subject,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         new_subject=request.data
#         ser=SubjectSerializer(data=new_subject)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def patch(self,request):
#         instance=Subject.objects.get(id=request.GET.get('subjectId'))
#         ser=SubjectSerializer(instance,data=request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def delete(self,request):
#         current_subject=Subject.objects.get(id=request.GET.get('subjectId'))
#         current_subject.delete()
#         return Response({"messages":"lesson deleted"})  
    


# class AdminLessonView(APIView):
#     permission_classes=[IsAdminUser]
#     def get (self,request):
#         lesson_id=request.GET.get('lessonId')
#         subject_id=request.GET.get('subjectId') 
#         if subject_id:
#             lesson=Lesson.objects.filter(subject=subject_id)
#             ser=LessonSerializer(lesson,many=True)
#             return Response(ser.data)            
#         elif lesson_id:
#             lesson=Lesson.objects.get(id=lesson_id)    
#             ser=LessonSerializer(lesson)
#             return Response(ser.data)            

#         else:
#             lesson=Lesson.objects.all()
#             ser=LessonSerializer(lesson,many=True)
#             return Response(ser.data)
#     def post(self,request):
#         new_lesson=request.data
#         ser=LessonSerializer(data=new_lesson)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def patch(self,request):
#         instance=Lesson.objects.get(id=request.GET.get('lessonId'))
#         ser=LessonSerializer(instance,data=request.data,partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
#     def delete(self,request):
#         current_lesson=Lesson.objects.get(id=request.GET.get('lessonId'))
#         current_lesson.delete()
#         return Response({"messages":"lesson deleted"})  
    

# class AdminAssignmentView(APIView):
#     permission_classes=[IsAdminUser]
#     def get (self,request):
#         assignment_id=request.GET.get('AssignmentId')
#         completed_task=request.GET.get('completed')
#         incompleted_task=request.GET.get('incomplet')        
#         if assignment_id:
#             assignment=AssignmentTask.objects.get(id=assignment_id)
#             ser=TaskSerializer(assignment)
#             return Response(ser.data)
#         elif completed_task:    
#             assignment=AssignmentTask.objects.filter(is_completed=True)
#         elif incompleted_task:    
#             assignment=AssignmentTask.objects.filter(is_completed=False)
#         else:    
#             assignment=AssignmentTask.objects.all()
#         ser=TaskSerializer(assignment,many=True)
#         return Response(ser.data)
#     def post(self, request):
#         new_task = request.data
#         student_ids = request.data.getlist('students')  # ✅ expects a list of IDs

#         ser = TaskSerializer(data=new_task)
#         if ser.is_valid():
#             assignment = ser.save()
#             for student_id in student_ids:
#                 try:
#                     student = StudentProfile.objects.get(id=int(student_id))  # cast just to be safe
#                     AssignmentSubmission.objects.create(
#                         student=student,
#                         assignment=assignment
#                     )
#                 except StudentProfile.DoesNotExist:
#                     continue

#             return Response(TaskSerializer(assignment).data)

#         return Response(ser.errors, status=400)



# class AdminSubmissionView(APIView):
#     def get(self,request):
#         assignment_id=request.GET.get('assignmentId')
#         submission_id=request.GET.get('submissionId')
#         if assignment_id:
#             submission=AssignmentSubmission.objects.filter(assignment=assignment_id)
#             ser=AssignmentSubmissionSerializer(submission,many=True)

#         elif submission_id:
#             submission=AssignmentSubmission.objects.get(id=submission_id)   
#             ser=AssignmentSubmissionSerializer(submission)     
#         else:
#             submission=AssignmentSubmission.objects.all()
#             ser=AssignmentSubmissionSerializer(submission,many=True)
#         return Response(ser.data)
#     def patch(self,request):
#         submission_id=request.GET.get('submissionId')
#         inst=AssignmentSubmission.objects.get(id=submission_id)
#         if not inst:
#             return Response("assignment id requierd")
#         ser=AssignmentSubmissionSerializer(inst,request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response (ser.data)
#         return Response(ser.errors)
    

    



# class adminDashboardView(APIView):
#     permission_classes = [IsAdminUser]

#     def get(self, request):
#         result = {}

#         # General counts
#         users = CustomUser.objects.all().count()
#         profile_completed = StudentProfile.objects.all().count()
#         courses = Course.objects.all().count()
#         subjects = Subject.objects.all().count()
#         lessons = Lesson.objects.all().count()

#         # Assignments
#         total_assignments = AssignmentTask.objects.count()
#         completed_assignments = AssignmentSubmission.objects.filter(is_completed=True).count()
#         incomplete_assignments = AssignmentSubmission.objects.filter(is_completed=False).count()
#         valuated_submission = AssignmentSubmission.objects.filter(mark__isnull=False).count()
#         notvaluated_submission = AssignmentSubmission.objects.filter(mark__isnull=True).count()

#         # Populate result dictionary
#         result['total_users'] = users
#         result['profile_completed'] = profile_completed
#         result['total_courses'] = courses
#         result['total_subjects'] = subjects
#         result['total_lessons'] = lessons
#         result['total_assignments'] = total_assignments
#         result['completed_submissions'] = completed_assignments
#         result['incomplete_submissions'] = incomplete_assignments
#         result['evaluated_submissions'] = valuated_submission
#         result['not_evaluated_submissions'] = notvaluated_submission

#         return Response(result)
    

# class AdminLeaderBoardView(APIView):
#     permission_classes=[IsAdminUser]
#     def get(self,request):
#         leaderboard=Leaderboard.objects.all()
#         ser=LeaderBoardSerializer(leaderboard, many=True)
#         return Response(ser.data)













from django.shortcuts import render
from rest_framework.views import APIView
from account.models import CustomUser
from account.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Q
from student.models import StudentProfile, AssignmentTask, AssignmentSubmission, Leaderboard
from student.serializers import StudentProfileSerializer, AssignmentSubmissionSerializer, TaskSerializer, LeaderBoardSerializer
from .models import Course, Subject, Lesson
from .serializers import CourseSerializer, SubjectSerializer, LessonSerializer
from rest_framework import status


class UsersListAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        user_keyword = request.GET.get('user')
        users = CustomUser.objects.filter(email__istartswith=user_keyword) if user_keyword else CustomUser.objects.all()
        ser = CustomUserSerializer(users, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def patch(self, request):
        user_id = request.data.get('id')
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"message": "User ID is required"}, status=status.HTTP_404_NOT_FOUND)
        ser = CustomUserSerializer(user, request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentListAdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        student_keyword = request.GET.get("student")
        course_keyword = request.GET.get("course")

        queryset = StudentProfile.objects.all()
        if student_keyword:
            queryset = queryset.filter(full_name__icontains=student_keyword)
        if course_keyword:
            queryset = queryset.filter(course_id=course_keyword)

        serializer = StudentProfileSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AdminCourseView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        course = Course.objects.all()
        ser = CourseSerializer(course, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = CourseSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            course = Course.objects.get(id=request.GET.get('courseId'))
        except Course.DoesNotExist:
            return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = CourseSerializer(course, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            course = Course.objects.get(id=request.GET.get('courseId'))
            course.delete()
            return Response({"message": "Course deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({"message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)


class AdminSubjectView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        course_id = request.GET.get('courseId')
        subject = Subject.objects.filter(course=course_id) if course_id else Subject.objects.all()
        ser = SubjectSerializer(subject, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = SubjectSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            instance = Subject.objects.get(id=request.GET.get('subjectId'))
        except Subject.DoesNotExist:
            return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = SubjectSerializer(instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            subject = Subject.objects.get(id=request.GET.get('subjectId'))
            subject.delete()
            return Response({"message": "Subject deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)


class AdminLessonView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        lesson_id = request.GET.get('lessonId')
        subject_id = request.GET.get('subjectId')

        if subject_id:
            lessons = Lesson.objects.filter(subject=subject_id)
            ser = LessonSerializer(lessons, many=True)
        elif lesson_id:
            lesson = Lesson.objects.get(id=lesson_id)
            ser = LessonSerializer(lesson)
        else:
            lessons = Lesson.objects.all()
            ser = LessonSerializer(lessons, many=True)

        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = LessonSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            lesson = Lesson.objects.get(id=request.GET.get('lessonId'))
        except Lesson.DoesNotExist:
            return Response({"message": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = LessonSerializer(lesson, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            lesson = Lesson.objects.get(id=request.GET.get('lessonId'))
            lesson.delete()
            return Response({"message": "Lesson deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Lesson.DoesNotExist:
            return Response({"message": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)


class AdminAssignmentView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        assignment_id = request.GET.get('AssignmentId')
        completed_task = request.GET.get('completed')
        incompleted_task = request.GET.get('incomplet')

        if assignment_id:
            assignment = AssignmentTask.objects.get(id=assignment_id)
            ser = TaskSerializer(assignment)
        elif completed_task:
            assignment = AssignmentTask.objects.filter(is_completed=True)
            ser = TaskSerializer(assignment, many=True)
        elif incompleted_task:
            assignment = AssignmentTask.objects.filter(is_completed=False)
            ser = TaskSerializer(assignment, many=True)
        else:
            assignment = AssignmentTask.objects.all()
            ser = TaskSerializer(assignment, many=True)

        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        ser = TaskSerializer(data=request.data)
        student_ids = request.data.getlist('students')

        if ser.is_valid():
            assignment = ser.save()
            for student_id in student_ids:
                try:
                    student = StudentProfile.objects.get(id=int(student_id))
                    AssignmentSubmission.objects.create(student=student, assignment=assignment)
                except StudentProfile.DoesNotExist:
                    continue
            return Response(TaskSerializer(assignment).data, status=status.HTTP_201_CREATED)

        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminSubmissionView(APIView):
    def get(self, request):
        assignment_id = request.GET.get('assignmentId')
        submission_id = request.GET.get('submissionId')

        if assignment_id:
            submissions = AssignmentSubmission.objects.filter(assignment=assignment_id)
            ser = AssignmentSubmissionSerializer(submissions, many=True)
        elif submission_id:
            submission = AssignmentSubmission.objects.get(id=submission_id)
            ser = AssignmentSubmissionSerializer(submission)
        else:
            submissions = AssignmentSubmission.objects.all()
            ser = AssignmentSubmissionSerializer(submissions, many=True)

        return Response(ser.data, status=status.HTTP_200_OK)

    def patch(self, request):
        submission_id = request.GET.get('submissionId')
        try:
            inst = AssignmentSubmission.objects.get(id=submission_id)
        except AssignmentSubmission.DoesNotExist:
            return Response({"message": "Submission not found"}, status=status.HTTP_404_NOT_FOUND)

        ser = AssignmentSubmissionSerializer(inst, request.data, partial=True)
        if ser.is_valid():
            updated_submission =ser.save()
            student = updated_submission.student
            mark = updated_submission.mark
            Leaderboard.objects.create(student_name=student,mark=mark)
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class adminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        result = {
            'total_users': CustomUser.objects.count(),
            'profile_completed': StudentProfile.objects.count(),
            'total_courses': Course.objects.count(),
            'total_subjects': Subject.objects.count(),
            'total_lessons': Lesson.objects.count(),
            'total_assignments': AssignmentTask.objects.count(),
            'completed_submissions': AssignmentSubmission.objects.filter(is_completed=True).count(),
            'incomplete_submissions': AssignmentSubmission.objects.filter(is_completed=False).count(),
            'evaluated_submissions': AssignmentSubmission.objects.filter(mark__isnull=False).count(),
            'not_evaluated_submissions': AssignmentSubmission.objects.filter(mark__isnull=True).count()
        }
        return Response(result, status=status.HTTP_200_OK)


class AdminLeaderBoardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        leaderboard = Leaderboard.objects.all()
        ser = LeaderBoardSerializer(leaderboard, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


from .models import Home
from .serializers import HomeSerialiser

# class HomeView(APIView):
#     def get(self, request):
#         try:
#             home = Home.objects.get(id=1)
#             serializer = HomeSerialiser(home)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Home.DoesNotExist:
#             return Response({'error': 'Home not found'}, status=status.HTTP_404_NOT_FOUND)

class HomeView(APIView):
    def get(self, request):  # ✅ Fixed typo
        try:
            home = Home.objects.all()
            serializer = HomeSerialiser(home,many=True)  # ✅ Removed many=True
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Home.DoesNotExist:
            return Response({'error': 'Home not found'}, status=status.HTTP_404_NOT_FOUND)