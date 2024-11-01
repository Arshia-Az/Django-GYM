from django.urls import path
from aboutUs_module import views

urlpatterns = [
    path('', views.about, name='about_us'),
]