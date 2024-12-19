from django.urls import path
from.import views

urlpatterns=[
    path('home/',views.members_home),
    #path('about/',views.members_about),
    path('addMember/',views.add_member),
    #path('addMemberByUrl/',views.add_member_by_url),
    path("addMultipleMember/",views.add_multiple_member),
    path('viewAllMembers/',views.view_members,name="view_members"),
    path('searchMember/',views.search_member),
    path('memberDetails/<int:id>',views.member_details),
    path('deleteMember/<int:id>/',views.deleteMember,name="deleteMember"),
    path('updateMember/<int:id>',views.updateMember,name="update_member"),
    path('testing/',views.testing),
    path('fruitsData/',views.fruitsData,name="fruitsData")
    
]
