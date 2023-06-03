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
def TwoD(request):
    """
        Trả về trang 2D
    """
    context ={}
    return render(request,'app/2D.html',context)
def ThreeD(request):
    """
        Trả về trang 3D
    """
    context ={}
    return render(request,'app/3D.html',context)
def Icon(request):
    """
        Trả về trang Icon
    """
    context ={}
    return render(request,'app/Icon.html',context)