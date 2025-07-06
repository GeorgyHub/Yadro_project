from django.urls import path, include
from django.conf import settings

from .views import my_profile

urlpatterns = [
    path('', my_profile, name='my_profile'),
]