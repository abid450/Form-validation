from django.shortcuts import render
from .models import todo
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        contact = todo()
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        text = request.POST.get('text')
        contact.Name=Name
        contact.Email=Email
        contact.password=Password
        contact.text=text
        contact.save()
        return HttpResponse("<h2>Thanks for Contact Us </h2>")
        
    return render(request,'index.html')



def about(request):
    return render(request,"about.html")

