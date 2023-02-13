from django.urls import path
from resume.views import *

urlpatterns = [
    path("", ProfileView.as_view(), name='profile')
]
