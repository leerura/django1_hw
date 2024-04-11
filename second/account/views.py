from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #유저 확인, 유저 생성
from django.http import HttpResponse



# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  #???
            login(request, user)
        return redirect('home')

def signup_func(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('home')

def login_view(request): #함수 이름을 login으로 하면 충돌 가능
    if request.method == 'GET':
        form = AuthenticationForm() #폼을 html에 전달합시다.
        return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect("home")
            
def logout_view(request): #함수 이름을 logout으로 하면 충돌 가능
    logout(request)
    return redirect('home')
            









    