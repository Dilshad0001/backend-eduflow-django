
from django.urls import path
from . import views

urlpatterns = [

    path('profile/',views.StudentprofileStudentView.as_view()),
    path('course/',views.StudentCourseView.as_view()),
    path('subject/',views.StudentSubjectView.as_view()),
    path('lesson/',views.StudentLessonView.as_view()),
    path('task/',views.StudentTaskView.as_view()),
    path('submission/',views.StudentSubmissionView.as_view()),
    path('leaderboard/',views.LeaderBoardStudentView.as_view()),

]
