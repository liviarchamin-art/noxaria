from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
    path("chat/", views.chat_api, name="chat_api"),
]
