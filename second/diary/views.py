from django.shortcuts import render,redirect, get_object_or_404 #redirect 저장 후 다시 상세보기로
from .models import Diary
from django.utils import timezone #pub_date 땜에
# Create your views here.

def home(request):
    diarys = Diary.objects.all()
    return render(request, "home.html", {"diarys":diarys , "count" : len(diarys)})

def create(request):
    return render(request, "create.html")

def detail(request, id):
    diary_detail = get_object_or_404(Diary,pk = id)
    return render(request , "detail.html", {'diary_detail' : diary_detail} ) 

def create_func(request):
    new_diary = Diary()
    new_diary.title = request.POST['title'] #id 사용 not name
    new_diary.pub_update = request.POST['date'] #timezone.now도 가능
    new_diary.writer = request.POST['writer']
    new_diary.body = request.POST['body']
    new_diary.save() #저장
    return redirect('detail', new_diary.id) #id보내야 됨
