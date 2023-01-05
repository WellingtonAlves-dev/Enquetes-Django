from django.urls import path, include
from . import views

app_name = "answer"

urlpatterns = [
    path("save/<int:id>", views.save_answer, name="save")
]