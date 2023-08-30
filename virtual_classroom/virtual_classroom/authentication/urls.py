from django.urls import re_path
from . import views

urlpatterns = [
    re_path('api/login/', views.LoginView.as_view(), name='sign_in'),
    re_path('api/register/', views.RegisterView.as_view(), name='sign_up'),
    re_path('login/', views.login_page, name='login'),
    re_path('register/', views.register_page, name='register'),
]