from django.urls import path
from preview.views import home
urlpatterns = [
    path('catalog',home ),
   
]
