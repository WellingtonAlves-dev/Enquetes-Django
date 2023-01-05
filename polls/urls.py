from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path("", views.list_polls, name="list"),
    path("enquete/<int:id>", views.poll, name="poll")
]