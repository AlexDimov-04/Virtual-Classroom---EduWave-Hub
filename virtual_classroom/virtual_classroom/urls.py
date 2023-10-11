from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('virtual_classroom.main.urls')),
    path('profile/', include('virtual_classroom.authentication.urls')),
    path('accounts/', include('allauth.urls')),

]
