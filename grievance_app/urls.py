from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('submit/', views.submit_grievance, name='submit'),

    path('success/', views.success, name='success'),

    path('register/', views.register, name='register'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('track/', views.track_complaint, name='track'),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path('logout/', views.logout_user, name='logout'),
]