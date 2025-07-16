
from django.urls import path
from . import views

urlpatterns = [

    path('register/',views.Register.as_view()),
    path('login/',views.Login.as_view()),
    path('',views.Login.as_view()),
    path('self/',views.SelfUserView.as_view()),
    # path('profile/',views.student)
]
