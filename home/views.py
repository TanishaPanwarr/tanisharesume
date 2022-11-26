from django.shortcuts import render
from django.shortcuts import redirect, render
from .models import Emp
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from tanuresume.settings import EMAIL_HOST_USER
def index(request):
    return render(request,'index.html')

def feedback(request):
    if request.method=='POST':
        e=Emp()
        e.name=request.POST['name']
        e.email=request.POST['email']
        e.subject=request.POST['subject']
        e.message=request.POST['message']
        e.save()
        email=request.POST['email']
        name=request.POST['name']
        subject = 'Thank You For Your Responce'
        message = 'Hello i am Tanisha !! Hope you are well and I am a full-stack Web Developer with a passion for web application development. Dedicated to dirving innovation with the ability to follow industry and technological trends to acheive Organizational goals.'
        recepient = email
        recepient1 = name
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], [recepient1])
        return render(request, 'index.html', {'recepient': recepient})
    else:
        return render(request,'index.html')
def page_not_found(request,exception):
    return render(request,'pagenotfound.html')

