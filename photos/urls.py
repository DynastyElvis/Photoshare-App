from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('location/',views.location,name='location'),
    path('photo/<str:pk>add/',views.viewPhoto,name='photo'),
    path('add/',views.addPhoto,name='add'),
]