from django.contrib import admin
from django.urls import path
from django.shortcuts import render  # Import render here
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name='register'),
    path('login/', accounts_views.user_login, name='login'),
    path('', lambda request: render(request, 'home.html'), name='home'),  # This line now works
]

