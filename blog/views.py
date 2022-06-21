from django.shortcuts import render, redirect
from .models import  Todo
from .forms import  TodoForm
from django.views.decorators.http import require_POST


def index(request):
    todo = Todo.objects.all()
    form = TodoForm()
    return  render(request, 'index.html', {'todo_list': todo ,'form': form})

@require_POST
def addToDo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()
    return redirect('/')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    if todo.complate:
        todo.complate = False
        todo.save()
    else:
        todo.complate = True
        todo.save()
    return redirect('index')



def delete_complate(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')


