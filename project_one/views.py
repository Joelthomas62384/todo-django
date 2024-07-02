from django.shortcuts import render,redirect
from app.models import *
from django.db.models import F
from django.http import JsonResponse



def home(request):
    tasks = Task.objects.filter(deleted=False).order_by(F('done').asc(), '-id')[:20]
    context = {
        'tasks':tasks
    }
    return render(request,"index.html",context)


def about(request):
    return render(request,'about.html')


def tasks(request):
    if request.method == "POST":
        task = request.POST.get('task')
        date = request.POST.get('date')
        time = request.POST.get('time')

        tasks = Task(task=task,date=date,time=time)
        tasks.save()

    



    return redirect('home')





def task_done(request, id):
    task = Task.objects.get(id=id)
    task.done = True
    task.save()
    return JsonResponse({"status": "success"})

def task_delete(request, id):
    task = Task.objects.get(id=id)
    task.deleted = True
    task.save()
    return JsonResponse({"status": "success"})
