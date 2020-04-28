from django.shortcuts import render, redirect
from .models import TodoListItem

def todoappView(request):
    """The home page for the Todo List App."""
    all_todo_items = TodoListItem.objects.all()
    context = { 'all_items' : all_todo_items }
    return render(request, 'todoapp/todo_list.html', context)

def addTodoItem(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return redirect('todoapp:todoappView')

def deleteTodoItem(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return redirect('todoapp:todoappView')
