from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("projects/create", views.projectsForm, name="projectForm"),
    path("tasks/", views.tasks, name="tasks"),
    path("create-task/", views.create, name="create_tasks"),
]
