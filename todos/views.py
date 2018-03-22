from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'add.html')

def delete(request,id):
    # if (request.method=='POST'):
    reply = Todo.objects.get(id=id)
    reply.delete()

    return redirect('/todos')
    #else:
        #return render(request, 'delete.html')
def updater(request):
    if(request.method == 'POST'):
        ids = request.POST['id']
        tod = Todo.objects.get(id=ids)

        title = request.POST['title']
        text = request.POST['text']

        tod.title=title
        tod.text=text
        tod.save()
        return redirect('/todos')

def update(request,id):
    tod = Todo.objects.get(id=id)
    print "asds"

    # if(request.method == 'POST'):
    #     title = request.POST['title']
    #     text = request.POST['text']

    #     tod.update(title=title,text=text)
    #     todo.save()
    #     return redirect('/todos')

    context = {
        'todo':tod
    }
    return render(request, 'update.html', context)

