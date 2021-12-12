from django.urls import path,include
from . import views
urlpatterns =[
    path('baabtra',views.Baabfn,name='baabtra'),
    path('course',views.secfn,name='course'),
    path('contact',views.thirdfn,name='contact')
    ]