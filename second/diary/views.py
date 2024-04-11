from django.shortcuts import render,redirect, get_object_or_404 #redirect 저장 후 다시 상세보기로
from .models import Diary
from django.utils import timezone #pub_date 땜에
from .forms import DiaryForm

# Create your views here.

def home(request):
    diarys = Diary.objects.all().order_by('id')
    count = len(diarys)   #diarys.count !! 라는 함수도 있음
    count = int(count)
    #select의 value에 따라 뭐 보낼지 정해ㅐㅐㅐㅐㅐ
    old_diarys = diarys
    new_diarys = diarys.reverse()
    data = {"diarys":new_diarys , "count" : count}
    return render(request, "home.html", data)

def create(request):
    form = DiaryForm
    return render(request, "create.html", {'form':form})

def detail(request, id):
    diary_detail = get_object_or_404(Diary, pk = id)
    return render(request , "detail.html", {'diary_detail' : diary_detail} ) 

def create_func(request):
    form = DiaryForm(request.POST,request.FILES)
    if form.is_valid():
        new_diary = form.save(commit=False) #임시저장
        new_diary.pub_update = timezone.now()
        new_diary.save()
        return redirect('detail', new_diary.id) #id보내야 됨
    else:
        return redirect('home') # 정보가 기입되지 않았다는 알림창이 더 괜찮을 듯

    #new_diary = Diary()
    #new_diary.title = request.POST['title'] #id 사용 not name
    #new_diary.pub_update = timezone.now() #timezone.now도 가능
    #new_diary.writer = request.POST['writer']
    #new_diary.body = request.POST['body']
    #new_diary.image = request.FILES['image'] #이미지는 다른 애들과 다르게
    #new_diary.save() #저장                                                  

def update(request, update_id):
    diary_update = get_object_or_404(Diary, pk=update_id)
    return render(request, "update.html", {'diary_update':diary_update})

def update_fuc(request, to_id):
    diary_to_update = get_object_or_404(Diary, pk=to_id)
    diary_to_update.title = request.POST['title'] #id 사용 not name
    diary_to_update.pub_update = timezone.now #timezone.now도 가능
    diary_to_update.writer = request.POST['writer']
    diary_to_update.body = request.POST['body']
    diary_to_update.save() #저장
    return redirect('detail', diary_to_update.id )      

def delete(request, delete_id):
    diary_to_delete = get_object_or_404(Diary, pk=delete_id)
    diary_to_delete.delete()
    return redirect('home')
