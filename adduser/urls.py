from django.urls import path

from . import views
urlpatterns = [
    path('addInterestUsers', views.addInterestUser, name='addInterestUser'),
]
