from django import forms
from .models import Task

#Here we'll handle task creation and update
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','completed']