from django.urls import path
from . import views

urlpatterns=[
    path('adminwelcome/',views.adminhome,name="adminhome"),
    path('adminsessionred/',views.adminlogout,name="adminlogout"),
    path('viewstudent/',views.viewstudent,name="viewstudent"),
    path('viewenquiry/',views.viewenquiry,name="viewenquiry"),
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),
    path('viewcomplain/',views.viewcomplain,name="viewcomplain"),
    path('studymaterial/',views.studymaterial,name="studymaterial"),
    path('move/',views.move,name="move"),

]