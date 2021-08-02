from django.shortcuts import render,redirect
from home1.models import userupload
from ani01.forms import studentforms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth

def upload(request):
    if request.method=="POST":
        if request.POST.get('author') and request.POST.get('about') and request.POST.get('img'):
                saverecord = userupload()
                saverecord.author=request.POST.get('author')
                saverecord.description=request.POST.get('description)
                saverecord.image=request.POST.get('img')
                saverecord.save()
                messages.success(request,'save messages successfully!!')
                return render(request,'index.html')

    else:
        return render(request,'upload.html')


def dashboard(request):
    dashboard=userupload.objects.all()
    return render(request,'dashboard.html',{'userupload': dashboard})

def editstudentdetails(request,id):
    displaystudent = userupload.objects.get(id=id)
    return render(request,'edit.html',{"userupload":displaystudent})

def updatestudentdetails(request,id):
    updatestudentdetails=userupload.objects.get(id=id)
    form=studentforms(request.POST, request.FILES, instance=updatestudentdetails)
    if form.is_valid():
        print(form)
        form.save()
        messages.success(request,'Record Updated Successfully...')
        return render(request,'edit.html',{'userupload':updatestudentdetails})
    

def delstudent(request,id):
    deletestudent= userupload.objects.get(id=id)
    deletestudent.delete()
    dashboard=userupload.objects.all()
    return render(request,'dashboard.html',{'userupload': dashboard})

# def upload_question(request):
#     if request.method=="POST":
#         question=question()
#         form=Question_form(request.POST,instance=question)
#         if form.is_valid:
#             form.save()
            
    


