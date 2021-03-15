from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.utils import timezone
import datetime
import time
from .models import Todo, Subtasks


def home(request):
    if request.method == "POST":
        # gets the selected todo objects
        todo_ids = request.POST.getlist("todo", False)
        
        # deletes all of the selected todo objects
        for i in todo_ids:
            Todo.objects.filter(id=int(i)).delete()
    

    for i in Todo.objects.all():
        if (i.date_end - timezone.now()).total_seconds() < 0:
            i.is_due = True
            i.save()
        else:
            i.is_due = False
            i.save()
    
    context = {"todos": Todo.objects.all()}
    return render(request, 'todoapp/base.html', context)

def todoAdd(request):

    if request.method == "POST":
        # Gets the posted content
        content = request.POST.get("content", False)
        date = request.POST.get("date", False)
        details = request.POST.get("details", False)
        subtasks = request.POST.getlist("subtask", False) # atceries par getlist

        # formats the time and passes it to the database
        dateTimeObj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M')
        newTodo = Todo(content=f"{content}", date_end=dateTimeObj, details=details)
        newTodo.save()

        # Creates all objets of the subtask
        for subtask in subtasks:
            newSubtask = Subtasks(todo=newTodo, content=subtask)
            newSubtask.save()

        return redirect("todo:home")

    return render(request, "todoapp/todoadd.html")

# Editing in the details section
def todoDetails(request, pk):
    
    if request.method == "POST":
        details = request.POST.get("details", False)
        subtasks = request.POST.getlist("subtask", False)

        obj = Todo.objects.get(id=pk)
        obj.details = details
        obj.save()

        Subtasks.objects.filter(todo=obj).delete()

        for subtask in subtasks:
            newSubtask = Subtasks(todo=obj, content=subtask)
            newSubtask.save()

        
        return redirect("todo:home") 


    todoObject = Todo.objects.get(id=pk) # the todo passed to the page
    todoSubtasks = Subtasks.objects.filter(todo=todoObject) # the subtasks attached to the todo

    context = {"object": todoObject, "subtasks": todoSubtasks}
    timeLeft = (context["object"].date_end - timezone.now()).total_seconds()
    # wanrltw = datetime.timedelta(microseconds=0)
    # print((context["object"].date_end + wanrltw).total_seconds)
    late = False

    
    if timeLeft < 0 :
        timeLeft = timeLeft * -1
        late = True

    day = int(timeLeft // (24 * 3600))
    timeLeft = timeLeft % (24 * 3600)
    hour = int(timeLeft // 3600)
    timeLeft %= 3600
    minutes = int(timeLeft // 60)
    timeLeft %= 60
    second = int(timeLeft)

    if late == True:
        context["timeStr"] = f"{day} days {hour}:{minutes}:{second} LATE"
    else:
        context["timeStr"] = f"{day} days {hour}:{minutes}:{second}"
    
    return render(request, "todoapp/todo_detail.html", context=context)
        