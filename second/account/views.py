from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #유저 확인, 유저 생성
from django.http import HttpResponse



# Create your views here.

def signup(request):
    return render(request, 'signup.html')

def signup_func(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return redirect('home')

def login(request):
    form = AuthenticationForm() #폼을 html에 전달합시다.
    return render(request, 'login.html', {'form':form})

def login_func(request):
    username = request.POST['username']
    password = request.POST['password']
    
    # 사용자 인증 시도
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        # 인증 성공: 사용자를 로그인 처리하고 성공 메시지를 반환합니다.
        #login(request, user)
        return HttpResponse("로그인 성공!")
    else:
        # 인증 실패: 실패 메시지를 반환합니다.
        return HttpResponse("로그인 실패. 사용자 이름 또는 비밀번호가 잘못되었습니다.")

    