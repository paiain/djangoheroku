from django.urls import path 
from pages.views import about, contect, index,persons

urlpatterns = [
    path('' ,index),
    path('about/', about),
    path('contect/',contect),
    path('persons', persons),
]