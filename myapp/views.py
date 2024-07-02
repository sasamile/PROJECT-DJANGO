from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateNewTaskForm, CreateNewProjectForm


# Create your views here.
def index(request):
    title = "Hello World!!"
    return render(request, "index.html", {"title": title})


def about(request):
    return render(request, "about.html")


def projects(request):
    project = Project.objects.all()
    return render(request, "projects.html", {"project": project})


def projectsForm(request):
    if request.method == "GET":
        form = CreateNewProjectForm()
        return render(request, "formprojects.html", {"form": form})
    elif request.method == "POST":
        Project.objects.create(
            name=request.POST["name"],
        )
        return redirect("projects")


def tasks(request):
    task = Task.objects.all()
    return render(request, "task.html", {"task": task})


def create(request):
    if request.method == "GET":
        form = CreateNewTaskForm()
        return render(request, "create_task.html", {"form": form})
    elif request.method == "POST":
        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=1,
        )
        return redirect("tasks")
