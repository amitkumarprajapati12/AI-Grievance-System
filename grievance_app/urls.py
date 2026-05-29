from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'submit/',
        views.submit_grievance,
        name='submit'
    ),

    path(
        'success/',
        views.success,
        name='success'
    ),

]