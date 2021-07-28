from django.urls import path, include
from .api import RegisterAPI

urlpatterns = [
    path('api/auth/register', RegisterAPI.as_view())
]
