#-*-coding:utf-8-*-
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from eyegic.models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def global_setting(request):
    return {'EYEGIC_STATIC':settings.EYEGIC_STATIC}

def center(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'center.html')

def mybook(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    name=request.session['username']
    user=User.objects.get(phone=name)
    book=BookFavor.objects.filter(user=user)
    return render(request,'mybook.html',{'book':book})

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

    bookid=request.GET.get('bookid')
    book=Book.objects.get(id=bookid)
    user=User.objects.get(phone=request.session.get('username'))
    favor=BookFavor.objects.get(book=book,user=user)
    unit1 = BookText.objects.filter(unit__book=book).filter(unit__unitnum=1).order_by('textnum')
    unit2 = BookText.objects.filter(unit__book=book).filter(unit__unitnum=2).order_by('textnum')
    unit3 = BookText.objects.filter(unit__book=book).filter(unit__unitnum=3).order_by('textnum')
    unit4 = BookText.objects.filter(unit__book=book).filter(unit__unitnum=4).order_by('textnum')
    unit5 = BookText.objects.filter(unit__book=book).filter(unit__unitnum=5).order_by('textnum')

    return render(request,'bookdetail.html',{'favor':favor,'book':book,'unit1':unit1,'unit2':unit2,'unit3':unit3,'unit4':unit4,'unit5':unit5})

def context(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    textid=request.GET.get('textid')
    text=BookText.objects.get(id=textid)
    return render(request,'context.html',{'text':text})

def index(request):
    chinese = Book.objects.filter(subject='chinese')[:4]
    math = Book.objects.filter(subject='math')[:4]
    english = Book.objects.filter(subject='english')[:4]
    return render(request,'index.html',{'chinese':chinese,'math':math,'english':english})

def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user = User.objects.filter(phone=name).filter(password=password)
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
        user = User.objects.filter(phone=name)
        if user.exists():
            return HttpResponse('username already exist!')
        user=User(phone=name,password=password)
        user.save()
        return HttpResponse('regist success!')
    else:
        return render(request,'regist.html')

def category(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'category.html')

def cover(request):
    return render(request,'cover.html')

def makeanswer(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'makeanswer.html')

def myactivity(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'myactivity.html')

def mycomment(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'mycomment.html')

def mymessage(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'mymessage.html')

def search(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'search.html')

def mytree(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    return render(request,'mytree.html')

def logout(request):
    del request.session['username']
    return HttpResponse('you have logout')

def isLogin(request):
    return request.session.get('username',default=None) is not None

@csrf_exempt
def add_favor_book(request):
    bookid=request.POST.get('book_id')
    phone=request.session.get('username')
    user=User.objects.get(phone=phone)
    book=Book.objects.get(id=bookid)
    BookFavor.objects.get_or_create(user=user,book=book)
    return HttpResponse('add to favor success!')