from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import todo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
@login_required
def home(request):
    tasks = todo.objects.filter(user= request.user, is_completed = False)
    completed = todo.objects.filter(user=request.user, is_completed = True)
    context = {
        'now': datetime.now(),
        'tasks': tasks,
        'completed_tasks': completed
    }
    return render(request, 'home-todo.html', context)

@require_POST
def addTask(request):
    task = request.POST['text']
    todo.objects.create(user = request.user,
                        text=task)
    return redirect('home')

def mark_as_done(request, item_id):
    task = get_object_or_404(todo, pk=item_id)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('home')
def deleteTask(request, item_id):
    task = get_object_or_404(todo, pk=item_id)
    task.delete()
    return redirect('home')
def editTask(request, item_id):
    task = get_object_or_404(todo, pk=item_id, user=request.user)
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        is_completed = request.POST.get('is_completed') in ['True', 'true', '1', 'on']
        if text:
            task.text = text
            task.is_completed = is_completed
            task.save()
            return redirect('home')
    context = {'task': task}
    return render(request, 'edit.html', context)

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tasks = todo.objects.filter(user = request.user, text__icontains = searched)
        context = {
            'searched': searched,
            'tasks': tasks
        }
        return render(request, 'search.html', context)
    
    else:
        return render(request, 'search.html', {})