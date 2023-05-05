from django.urls import path
from . import views

urlpatterns = [
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('student_portal/', views.student_portal, name='student_portal'),
    path('student_home/', views.student_home, name='student_home'),
    path('register/', views.register, name='registration_register'),
    path('success/', views.registration_success, name='registration_success'),
]
