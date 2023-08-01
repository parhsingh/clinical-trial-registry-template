from django.urls import path
from . import views

app_name = 'userauth'

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('forgotpassword/', views.forgot_password, name='forgot password'),
    path('dashboard/passwordreset/', views.reset_password, name='password reset'),
    path('register/', views.register_user, name='register'),
    path('registerorganisation/', views.register_organisation, name='register organisation'),
    path('logout/', views.logout_user, name='logout'),
]