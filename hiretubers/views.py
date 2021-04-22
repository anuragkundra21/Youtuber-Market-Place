from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
# Create your views here.
def hiretuber(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        tubers_name=request.POST['tubers_name']
        email=request.POST['email']
        phone=request.POST['phone']
        state=request.POST['state']
        city=request.POST['city']
        message=request.POST['message']
        tubers_id=request.POST['tubers_id']
        users_id=request.POST['users_id']

        hiretuber=Hiretuber(first_name=first_name,last_name=last_name,tubers_name=tubers_name,email=email,phone=phone,state=state,city=city,message=message,tubers_id=tubers_id,users_id=users_id)
        hiretuber.save()
        messages.success(request,'Thanks For Reaching Us Out!')
        return redirect('youtubers')
