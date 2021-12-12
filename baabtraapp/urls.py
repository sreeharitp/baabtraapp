from django.urls import path,include
from . import views
urlpatterns =[
    path('apphome',views.Baabfn,name='apphome'),
    path('course',views.secfn,name='course'),
    path('contact',views.thirdfn,name='contact')
    ]