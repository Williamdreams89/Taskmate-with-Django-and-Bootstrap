from django.shortcuts import render,redirect
from todolist_app.forms import TodoForm
from django.contrib import messages
from todolist_app.models import Todolist
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def todolist(request):
    if request.method=="POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).task_manager = request.user
            form.save()
        messages.success(request,("Task added successfully!!"))
        return redirect('todolist')
    else:
        all_tasks = Todolist.objects.order_by('-task_date').filter(task_manager = request.user)
        context = {"all_tasks":all_tasks}
        return render(request, 'todolist.html', context)

@login_required
def done_task(request,task_id):
    task_obj = Todolist.objects.get(pk=task_id)
    if task_obj.task_manager == request.user:
        task_obj.done = True
        task_obj.save()
    else:
        messages.error(request,('Access Restricted ...You are not allowed!!'))
    return redirect('todolist')

@login_required
def pending_task(request,task_id):
    task_obj = Todolist.objects.get(pk=task_id)
    task_obj.done = False
    task_obj.save()
    return redirect('todolist')

@login_required
def delete_task(request,task_id):
    task_obj = Todolist.objects.get(pk=task_id)
    if task_obj.task_manager == request.user:
        task_obj.delete()
    else:
        messages.error(request,('Access Restricted ...You are not allowed!!'))
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method=="POST":
        task_obj = Todolist.objects.get(pk=task_id)
        form = TodoForm(request.POST or None, instance=task_obj)
        if form.is_valid():
            form.save()
        messages.success(request,("Changes saved succesfully!!!"))
        return redirect("todolist")
    else:
        task_obj = Todolist.objects.get(pk=task_id)
        context = {'task_obj':task_obj}
        return render(request, 'edit.html',context)



