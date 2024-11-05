# blog/urls.py
from django.urls import path
from .views import blog_list, blog_detail, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<int:post_id>/', blog_detail, name='blog_detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]





