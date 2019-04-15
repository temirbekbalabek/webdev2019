from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from api.models import TaskList, Task


def show_lists(request):
    taskLists = TaskList.objects.all()
    json_tasklists = [t.to_json() for t in taskLists]
    data = {
        'tasklists': json_tasklists,
    }
    return JsonResponse(json_tasklists, safe=False)
def n_list(request, num):
    try:
        taskList = TaskList.objects.get(id=num)
        json_tasklist = taskList.to_json()
    except TaskList.DoesNotExist as e:
        json_tasklist = str(e)

    data = {
        'tasklist': json_tasklist,
    }
    return JsonResponse(json_tasklist, safe=False)
def n_list_tasks(request, num):
    try:
        a = TaskList.objects.get(id=num)
    except TaskList.DoesNotExist as e:
        return JsonResponse({{'error': str(e)}}, safe=False)
    tasks = a.task_set.all()
    json_tasks = [c.to_json() for c in tasks]
    data = {
        'tasklist': json_tasks,
    }
    return JsonResponse(json_tasks, safe=False)

def index(request):
    taskLists = TaskList.objects.all()
    context = {
        'tasklists': taskLists
    }
    return render(request, 'index.html', context)