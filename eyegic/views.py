from django.shortcuts import render

# Create your views here.
def cover(request):
    return render(request,'cover.html')

def center(request):
    return render(request,'center.html')

def mybook(request):
    return render(request,'mybook.html')