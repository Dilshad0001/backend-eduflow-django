from rest_framework import serializers
from .models import StudentProfile,AssignmentTask,AssignmentSubmission,Leaderboard
# from adminuser.serializers import CourseSerializer


class StudentProfileSerializer(serializers.ModelSerializer):
    # course=CourseSerializer
    class Meta:
        model = StudentProfile
        fields = ['id', 'full_name', 'phone_number', 'course','user']

    def to_representation(self, instance):
        return {
            "id":instance.id,
            "full_name":instance.full_name,
            "phone_number":instance.phone_number,
            "course":instance.course.course_name,
            "user":instance.user.email,
        }
    


class TaskSerializer(serializers.ModelSerializer):
    # students = serializers.PrimaryKeyRelatedField(queryset=StudentProfile.objects.all(),many=True)
    class Meta:
        model=AssignmentTask
        fields = ["id","students","task_name","task_file","description","uploaded_at","submission_deadline"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["students"] = [
            {
                "id": student.id,
                "full_name": student.full_name
            }
            for student in instance.students.all()
        ]
        return rep
    # def to_representation(self, instance): 
    #     request_user = self.context.get('user')
    #     try:
    #         k=StudentProfile.objects.get(user=request_user)
    #         student_list=[{"full_name":k.full_name}]
    #         user_="student"
    #     except StudentProfile.DoesNotExist:
    #         student_list=[{
    #             "full_name":st.full_name}for st in instance.students.all()
    #         ] 
    #         user_="teacher"
    #     ret={
    #     "id": instance.id,      
    #     "students":student_list,
    #     "task_name": instance.task_name,
    #     "task_file": instance.task_file.url if instance.task_file else None, 
    #     "description": instance.description,
    #     "uploaded_at": instance.uploaded_at,
    #     "submission_deadline": instance.submission_deadline,
    #     }
    #     if user_=="teacher":
    #         ret['blocked_students']=[{"full_name":s.full_name} for s in instance.blocked_students.all()]
    #     return ret


    # def create(self, validated_data):
    #     students = validated_data.pop('students', [])
    #     blocked_students = validated_data.pop('blocked_students', [])
    #     print("students = ", students)
    #     print("blocked_students = ", blocked_students)
    #     new_data = AssignmentTask.objects.create(**validated_data)
    #     new_data.students.set(students)
    #     new_data.blocked_students.set(blocked_students)
    #     assigned_students_set = set(new_data.students.all())
    #     blocked_students_set = set(new_data.blocked_students.all())
    #     unblocked_students = assigned_students_set - blocked_students_set
    #     print("Unblocked students: ", unblocked_students)
    #     k=StudentProfile.objects.get(id=8)
    #     if k in blocked_students:
    #         print("blockeed")  
    #     print("k in ser",k)
    #     return new_data

    # def update(self, instance, validated_data):
    #     instance.task_name=validated_data.get('task_name',instance.task_name)
    #     instance.task_file=validated_data.get('task_file',instance.task_file)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.submission_deadline=validated_data.get('submission_deadline',instance.submission_deadline)
    #     if 'students' in validated_data:
    #         instance.students.set(validated_data['students'])
    #     instance.save()
    #     return instance    






class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ["id","student","assignment","file","submitted_at","status","mark","is_completed"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "student": instance.student.full_name,
            "assignment": instance.assignment.task_name,
            "file": instance.file.url if instance.file else None,
            "submitted_at": instance.submitted_at,
            "status": instance.status,
            "mark": instance.mark,
            "is_completed":instance.is_completed
        }


    def update(self, instance, validated_data):
        instance.mark=validated_data.get('mark',instance.mark)
        instance.save()
        return instance


class studentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ["id","student","assignment","file","submitted_at","status","mark","is_completed"]

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "student": instance.student.full_name,
            "assignment": instance.assignment.task_name,
            "file": instance.file.url if instance.file else None,
            "submitted_at": instance.submitted_at,
            "status": instance.status,
            "mark": instance.mark,
            "is_completed":instance.is_completed
        }


    def update(self, instance, validated_data):
        instance.file=validated_data.get('file',instance.file)
        instance.status="submitted"
        instance.is_completed=True
        instance.save()
        return instance

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leaderboard
        fields=['student_name','mark']
    def to_representation(self, instance):

        rep = super().to_representation(instance)
        rep["student_name"] = instance.student_name.full_name
        return rep