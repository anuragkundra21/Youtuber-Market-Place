from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact_tuber(request):
    if request.method == 'POST':
        name=request.POST['name']
        company_name=request.POST['company_name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        users_id=request.POST['users_id']
        subject=request.POST['subject']

        contact=Contact(name=name,company_name=company_name,email=email,message=message,subject=subject,users_id=users_id,phone=phone)
        contact.save()
        return redirect('home')
