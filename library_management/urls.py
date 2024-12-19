from django.urls import path
from .import views

urlpatterns=[
   path('',views.home,name="library_home"),
   path('testing/',views.testing),
   path('addProfile/<int:id>/',views.addProfile,name="addProfile"),
   path('addBook/',views.addBook , name='add_book'),
   path('status/',views.library_status, name="library_status")
]