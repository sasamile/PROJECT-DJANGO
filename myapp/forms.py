from django import forms


class CreateNewTaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description de la tarea", widget=forms.Textarea)
    
class CreateNewProjectForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
