# courses/urls.py
from django.urls import path
from .views import course_list, course_detail, payment

urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('<int:course_id>/payment/', payment, name='payment'),
]
