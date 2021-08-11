from django.urls import path
from .views import *

urlpatterns = [
    path("", users_api),
    path("login", get_token),
]