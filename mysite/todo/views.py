from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, template_name = 'todo/index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(username = username, first_name = firstname, last_name = lastname, email = email, password = password)
        except:
            return HttpResponse('user with these enteties already exist please enter different enteties')
        else:
            user.save()
            return HttpResponse('user created')

        
    elif request.method == 'GET':
        return redirect('todo:index')