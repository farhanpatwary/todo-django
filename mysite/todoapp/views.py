from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoItem

def todoView(request):
    all_todos = todoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items':all_todos})

def addTodo(request):
    new_todo = todoItem(content = request.POST['content'])
    new_todo.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    item_to_delete = todoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')