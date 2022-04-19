from django.urls import path
from .views import *

urlpatterns = [
    path('about/',AboutpageView.as_view(),name='about'),
    path('',HomepageView.as_view(),name='home'),
]
