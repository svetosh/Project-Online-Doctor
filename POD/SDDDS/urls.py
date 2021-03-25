from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.index, name='index'),
]
