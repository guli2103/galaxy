from django.urls import path
from .views import *
from backend.views import *

urlpatterns = [
   path("", home, name=""),
   path('about.html/', AboutView.as_view(), name='about'),
   path('contact.html/', ContactView.as_view(), name='contact'),
   path('index-2.html/', Index2View.as_view(), name='index-2'),
   path('category.html/', CategoryView.as_view(), name='category'),
   path('post-details/',PostdetailsView.as_view(), name='post-details'),
   path('privacy/',PrivacyView.as_view(), name='privacy'),
   
]
