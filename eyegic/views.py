#-*-coding:utf-8-*-
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from eyegic.models import *
# Create your views here.
def center(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'center.html')

def mybook(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'mybook.html')

def bbsdetail(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'bbsdetail.html')
def comment(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'comment.html')

def feedback(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'feedback.html')

def makeComment(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'makecomment.html')

def setup(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'setup.html')

def subject_all(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    else:
        return render(request,'subject-all.html')

def bbs(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'bbs.html')

def bookdetail(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'bookdetail.html')

def context(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'context.html')

def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = User.objects.filter(nickname=name).filter(password=password)
        if user.exists():
            request.session['username']=name
            return HttpResponse('login success!')
        else:
            return HttpResponse('Password error or user not exist!')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = User.objects.filter(nickname=name)
        if user.exists():
            return HttpResponse('username already exist!')
        user=User(nickname=name,password=password)
        user.save()
        return HttpResponse('regist success!')
    else:
        return render(request,'regist.html')

def logout(request):
    del request.session['username']
    return HttpResponse('you have logout')

def isLogin(request):
    return request.session.get('username',default=None) is not None