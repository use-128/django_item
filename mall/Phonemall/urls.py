from django.urls import path
from Phonemall.views import index

urlpatterns = [
    path('index/',index),
]