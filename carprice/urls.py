from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path('car',views.car,name='car'),
    path('carprediction',views.prediction,name='prediction'),
]