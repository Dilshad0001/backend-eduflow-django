
from django.urls import path
from . import views

urlpatterns = [

    path('register/',views.register.as_view()),
    path('login/',views.logg.as_view()),
    path('self/',views.SelfUserView.as_view()),
    # path('profile/',views.student)
]
