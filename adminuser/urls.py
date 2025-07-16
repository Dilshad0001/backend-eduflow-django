
from django.urls import path
from . import views

urlpatterns = [

    path('users/',views.UsersListAdminView.as_view()),
    path('student/',views.StudentListAdminView.as_view()),
    path('course/',views.AdminCourseView.as_view()),
    path('subject/',views.AdminSubjectView.as_view()),
    path('lesson/',views.AdminLessonView.as_view()),
    path('task/',views.AdminAssignmentView.as_view()),
    path('submission/',views.AdminSubmissionView.as_view()),
    path('dashboard/',views.adminDashboardView.as_view()),
    path('leaderboard/',views.AdminLeaderBoardView.as_view()),


]
