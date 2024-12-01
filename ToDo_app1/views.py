from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm
from .models import Task
# Create your views here.
#A method to list tasks
#A method to create tasks

#to list tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'ToDo_app1/Task_List.html',{'tasks':tasks})
#to create tasks
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        #if form exists
        form = TaskForm()
        return render(request,'ToDo_app1/task_form.html',{'form':form})

def task_delete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'ToDo_app1/delete_confirm.html',{'task':task})

def task_update(request,pk):
     task = get_object_or_404(Task, pk=pk)
     if request.method == 'POST':
         form = TaskForm(request.POST, instance=task)
         if form.is_valid():
             form.save()
             return redirect('task_list')
         else:
             form = TaskForm(instance=task)
             return render(request,'ToDo_app1/task_form.html',{'form':form})
