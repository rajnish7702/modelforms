from django.urls import path
from . import views

urlpatterns = [
    path('', views.empdata, name='empdata'),
]