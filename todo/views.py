




from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpRequest,HttpResponse
from todo.models import Todo
from todo.forms import Todoform
# Create your views here.

def index(request):
    todos=Todo.objects.all()
    context={
        'todos':todos
    }
    return render(request,'index.html',context)


def add_todo(request):
    if request.method == 'POST':
        form=Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Todoform()
    return render(request,'add_todo.html',{'form':form})


def update_todo(request,pk):
    todo=Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form=Todoform(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Todoform(instance=todo)
    return render(request,'update_todo.html',{'form':form})

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')