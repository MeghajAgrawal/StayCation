from django.shortcuts import render,redirect
from django.contrib import messages
from .update import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):
    if request.method == "POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            msg=request.POST["message"]
            send_mail('Contact Form',msg,settings.EMAIL_HOST_USER,['meghajagrawal12@gmail.com'],fail_silently=False)
            messages.info(request,'Message Sent')
    form=ContactForm()
    return render(request,'contact.html',{'form':form})