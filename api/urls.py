from django.urls import path
from . import views

urlpatterns = [
  path('v1/add', views.addNumbers),
  path('v1/multiply', views.multiplyNumbers)
]