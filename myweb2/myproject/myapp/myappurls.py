from django.urls import path
from . import views 


urlpatterns=[
    path('',views.index,name='index'),
    path('deleteemp/<empid>',views.deleteemp,name='deleteemp'),
    #path('ndpage',views.index2,name='ndpage'),
    path('updateemp/<empid>',views.updateemp,name='updateemp'),
    path('update/',views.update,name='update'),
    ]