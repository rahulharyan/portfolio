from django.shortcuts import render,redirect
from base.models import Myprojects,Visiter
from django.contrib.auth.models import User
from .form import visiterForm



# Create your views here.

def home(request):

    return render(request ,'home.html')


def skills(request):
    
    return render(request , 'skills.html')

def about(request):
    return render(request , 'home.html')

def project(request):
    all_project=Myprojects.objects.all()
    context={
        'all_project':all_project
    }
    return render(request ,'project.html',context)

def experiance(request):
    return render(request , 'experiance.html')


def contact(request):
    success = False
    if request.method == 'POST':
        form=visiterForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form=visiterForm()
    else:
         form=visiterForm()

    context={
        'form':form,
        'success':success
    }
    return render(request ,'contact.html',context)
