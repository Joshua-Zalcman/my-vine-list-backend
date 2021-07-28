from django.contrib.auth import logout
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from .views import Logout

urlpatterns = [
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', Logout.as_view())
]
