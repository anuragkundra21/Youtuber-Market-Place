from django.urls import path
from  . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_users,name='logout'), #django has inbuilt logout view
    path('dashboard',views.dashboard,name='dashboard'),
]
