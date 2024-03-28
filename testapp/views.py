from django.shortcuts import render
from testapp.models import Hydjobs1,Bngjobs1,Punejobs1

def homepage_view(request):
    return render(request,'testapp/index.html')

def Hydjobs_view(request):
    jobs_list = Hydjobs1.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs1.html',my_dict)

def Bngjobs_view(request):
    jobs_list = Bngjobs1.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/bngjobs1.html',my_dict)

def Punejobs_view(request):
    jobs_list = Punejobs1.objects.all()
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/punejobs1.html',my_dict)

