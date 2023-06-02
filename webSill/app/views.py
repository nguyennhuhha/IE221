from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def base(request):
    '''
    Trả về base (header & footer)
    '''
    context={}
    return render(request, 'app/base.html',context) 
def home(request):
    """
        Trả về trang chủ home
    """
    context ={}
    return render(request,'app/home.html',context)