from django.urls import path

from . import views
urlpatterns = [
    path('addInterestUsers', views.addInterestUser, name='addInterestUser'),
    path('', views.check_site, name="check_site"),
]
