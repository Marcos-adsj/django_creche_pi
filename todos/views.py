from django.shortcuts import render

# listar as tarefas

def todo_list(request):
    return render(request, "todos/todo_list.html")
