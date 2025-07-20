from django.shortcuts import render,redirect
from base.models import Myprojects,Visiter
from django.contrib.auth.models import User
from .form import visiterForm
from django.core.mail import send_mail
from django.conf import settings


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
        form = visiterForm(request.POST)
        if form.is_valid():
            instance = form.save()
            success = True
            form = visiterForm()

            # Create the email content with all visitor details
            subject = 'New Contact Form Submission'
            message = f'''
New visitor form submission:

Full Name: {instance.full_name}
Email: {instance.email}
Phone: {instance.phone}
Subject: {instance.subject}
Message: {instance.message}
            '''
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['rahulharya2002@gmail.com'],  # You can add more emails in the list
                fail_silently=False,
            )
    else:
        form = visiterForm()

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

