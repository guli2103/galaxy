from django.urls import path
from .views import *
from backend.views import AboutView

urlpatterns = [
   path("", home),
   path('about.html/', AboutView.as_view())
]
