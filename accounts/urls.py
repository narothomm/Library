from django.urls import path
from .import views

urlpatterns=[
   path('',views.userHome,name="user_home"),
   path('register/',views.register,name='register'),
   path('login/',views.signIn,name='login'),
]