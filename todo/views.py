from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.

def home(request):
    todos = Task.objects.all().order_by("-date")
    return render(request, "home.html", {"todos": todos})

@csrf_exempt
def add_todo(request):
    content = request.POST["task"]
    if(content != ""):
        current_date = timezone.now()
        created_obj = Task.objects.create(date=current_date,task=content,is_completed=False)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    Task.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect("/")

def complete(request, todo_id):
    td = Task.objects.get(pk=todo_id)
    td.is_completed = True
    td.state = "COMPLETED"
    td.save()
    return HttpResponseRedirect("/")

def ongoing(request, todo_id):
    td = Task.objects.get(pk=todo_id)
    td.state = "ONGOING"
    td.save()
    return HttpResponseRedirect("/")