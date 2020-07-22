from django.shortcuts import render, redirect
from .models import TodoDatabase
from django.contrib import messages
import secrets

# For Viewing HomePage
def viewHomepage(request):

    if request.method == 'POST':
        task = request.POST['task']
        slug = secrets.randbits(16)
        
        # Handling Errors
        if len(task) < 5:
            messages.error(request, f'Type More Characters or Valid Task to Store in Database!!!')
            return redirect('homepage')

        todo = TodoDatabase(todo_task=task, slug=slug)
        todo.save()
        messages.success(request, f'Your Task Has Been Added in Database')
        return redirect('homepage')

    todoData = TodoDatabase.objects.all()[::-1]
    context = {'title':'TODO App', 'tasks':todoData}
        
    return render(request, 'todoApp/index.html', context)

def editTask(request, slug):

    todo = TodoDatabase.objects.get(slug=slug)
    taskName = todo.todo_task

    print(taskName)
    if request.method == 'POST':
        newTask = request.POST['task']

        if slug == todo.slug:
            todo.todo_task = newTask
            todo.save()
            messages.success(request, 'Your Changes has been Made Successfully!!!')
            return redirect('homepage')

    context = {'task':taskName}

    return render(request, 'todoApp/edit.html', context)

def removeTask(request, slug):

    todo = TodoDatabase.objects.get(slug=slug)
    todo.delete()
    return redirect('homepage')