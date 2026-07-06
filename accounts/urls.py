from django.urls import path
from .views import Register_View,Password_change_View,password_reset,password_reset_confirm,profile_user


urlpatterns = [
    path('',Register_View.as_view(),name='register'),
    path('change_form',Password_change_View.as_view(),name='password_change'),
    path('password_reset',password_reset.as_view(),name='password_reset'),
    path('password_reset_confirm',password_reset_confirm.as_view(),name='password_reset_confirm'),
    
    path('porfileUser',profile_user.as_view(),name='porfile')
]
