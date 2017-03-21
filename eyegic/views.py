#-*-coding:utf-8-*-
import datetime
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from eyegic.models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# Create your views here.

def global_setting(request):
    return {'EYEGIC_STATIC':settings.EYEGIC_STATIC}

def center(request):
    if not isLogin(request):
        return HttpResponseRedirect('login')
    user=User.objects.get(phone=request.session.get('username'))

    return render(request,'center.html',{'user':user})

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
    subject = request.GET.get('subject')
    if not subject:
        books=Book.objects.all()
    else:
        books=Book.objects.filter(subject=subject)
    return render(request,'subject-all.html',{'books':books})

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
    user=User.objects.get(phone=request.session.get('username'))
    text=BookText.objects.get(id=textid)
    question1=Questions.objects.filter(booktext=text).filter(type=1).get(num=1)
    question2=Questions.objects.filter(booktext=text).filter(type=1).get(num=2)
    question3=Questions.objects.filter(booktext=text).filter(type=2).get(num=1)
    question4=Questions.objects.filter(booktext=text).filter(type=2).get(num=2)
    question5=Questions.objects.filter(booktext=text).filter(type=3).get(num=1)
    question6=Questions.objects.filter(booktext=text).filter(type=3).get(num=2)
    answer1 = Answer.objects.filter(question=question1).get(user=user)
    answer2 = Answer.objects.filter(question=question2).get(user=user)
    answer3 = Answer.objects.filter(question=question3).get(user=user)
    answer4 = Answer.objects.filter(question=question4).get(user=user)
    answer5 = Answer.objects.filter(question=question5).get(user=user)
    answer6 = Answer.objects.filter(question=question6).get(user=user)

    return render(request,'context.html',{
        'text':text,'question1':question1,'question2':question2,
        'question3':question3,'question4':question4,
        'question5':question5,'question6':question6,
        'answer1':answer1,'answer2':answer2,
        'answer3':answer3,'answer4':answer4,
        'answer5':answer5,'answer6':answer6
    })

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
    if request.method=='GET':
        question_id=request.GET.get('questionid')
        question=Questions(id=question_id)
        return render(request,'makeanswer.html',{'question':question})
    else:
        question_id=request.POST.get('question_id')
        user=User.objects.get(phone=request.session.get('username'))
        question=Questions.objects.get(id=question_id)
        text_id=question.booktext.id
        comment=request.POST.get('comment')
        time=timezone.now()
        answer=Answer(user=user,question=question,answer=comment,time=time)
        answer.save()
        return HttpResponseRedirect('context.html?text_id='+text_id.__str__())


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