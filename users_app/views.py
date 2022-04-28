from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomedRegister
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method=="POST":
        register_form = CustomedRegister(request.POST)
        if register_form.is_valid():
            register_form.save()
        messages.success(request,("New User Created Successfully,Log in to get started!!"))
        return redirect('register')
    else:
        register_form = CustomedRegister()
        context = {"register_form":register_form}
        return render(request, 'register.html', context)
