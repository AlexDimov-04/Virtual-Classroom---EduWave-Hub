from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.ApiRegisterUserView.as_view(), name='api_register_view'),
    path('login/', views.ApiLoginUserView.as_view(), name='api_login_view'),
    path('logout/', views.ApiLogoutUserView.as_view(), name='api_logout_view'),
]