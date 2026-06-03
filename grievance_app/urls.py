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
        'download-pdf/<int:complaint_id>/',
        views.download_complaint_pdf,
        name='download_pdf'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path('logout/', views.logout_user, name='logout'),

    # API URLs for React
    path('api/complaints/', views.api_complaints, name='api_complaints'),

    path(
        'api/dashboard-stats/',
        views.api_dashboard_stats,
        name='api_dashboard_stats'
    ),
]