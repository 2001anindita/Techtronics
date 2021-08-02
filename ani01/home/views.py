from django.shortcuts import render,redirect
from home.models import *
from home.forms import *
from home1.models import userupload
from ani01.forms import studentforms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth



def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')


def user_login(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'You are sign in')
            return render(request,'index.html')
            
        else:
            messages.success(request,'login unsuccessful')
            return render(request,"checkout.html")
    else:

        return render(request,"checkout.html")


def contact(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('name') and request.POST.get('password'):
            if User.objects.filter(username=request.POST.get('name')).exists():
                messages.success(request, 'you have already login')
                return render(request,'checkout.html')
            else:
                saverecord = Quora()
                saverecord.email=request.POST.get('email')
                saverecord.name=request.POST.get('name')
                saverecord.password=request.POST.get('password')
                saverecord.save()
                user = User.objects.create_user(username=request.POST.get('name'),email=request.POST.get('email'),password=request.POST.get('password'))
                user.save()
                messages.success(request,'save messages successfully!!')
                return render(request,'checkout.html')
    
    else:
        return render(request,'contact.html')


def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def question_temp(request):
    return render(request,'question.html')

def answer_temp(request,id):
    data=question.objects.filter(id=id)
    form=Answer_form()
    return render(request,'answer.html', {'data': data, 'form': form})

def discuss_temp(request,id):
    data=question.objects.filter(id=id)
    form=Comment_form()
    return render(request,'discuss.html', {'data': data, 'form': form})

def lists(request):
    return render(request,'lists.html')

def dig(request):
    return render(request,'dig.html')

def ana(request):
    return render(request,'ana.html')

def micro(request):
    return render(request,'micro.html')

def cir(request):
    return render(request,'cir.html')

def ic(request):
    return render(request,'ic.html')

def pow(request):
    return render(request,'pow.html')

def opto(request):
    return render(request,'opto.html')

def semi(request):
    return render(request,'semi.html')

def emb(request):
    return render(request,'emb.html')

def wire(request):
    return render(request,'wire.html')

def nano(request):
    return render(request,'nano.html')


# def sports(request):
#     return render(request,'sports.html')

def ask(request):
    return render(request,'ask.html')

def ans(request):
    return render(request,'ans.html')

# def comment(request):
#     return render(request,'comment.html')


        
def upload(request):
    if request.method=="POST":
        if request.POST.get('author') and request.POST.get('description') and request.POST.get('img'):
            print(1)
            saverecord = userupload()
            saverecord.author=request.POST.get('author')
            saverecord.description=request.POST.get('description')
            saverecord.img=request.POST.get('img')
            saverecord.save()
            messages.success(request,'save messages successfully!!')
            return redirect('/')

    else:
        return render(request,'upload.html')


def dashboard(request):
    dashboard=userupload.objects.all()
    Question=question.objects.all()
    Answer=answer.objects.all()
    Comment=comment.objects.all()
    return render(request,'dashboard.html',{'userupload': dashboard, 'question': Question, 'answer': Answer, 'comment': Comment})
    

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

def upload_question(request):
    if request.method=="POST":
        question_model=question()
        form=Question_form(request.POST, instance=question_model)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
        else:
            pass
    else:
        return redirect("question")

def upload_answer(request):
    if request.method=="POST":
        # answer=answer()
        form=Answer_form(request.POST)
        print(form)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
        else:
            pass
    else:
        return redirect("answer")

def upload_comment(request):
    if request.method=="POST":
        # comment=comment()
        form=Comment_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect("dashboard")
        else:
            pass
    else:
        return redirect("comments")                
            


