from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path(
        'reset-password/', 
        auth_views.PasswordResetView.as_view(template_name="passwords/password_reset.html"), 
        name='reset_password'
    ),
    path(
        'reset-password-sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="passwords/password_reset_sent.html"), 
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="passwords/password_reset_form.html"), 
        name='password_reset_confirm'
    ),
    path(
        'reset-password-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="passwords/password_reset_done.html"), 
        name='password_reset_complete'
    ),
]