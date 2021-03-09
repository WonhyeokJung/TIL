from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('mail/', views.mail),
    path('lotto/', views.lotto),
]
