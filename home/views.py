from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from .models import Tasks

# Create your views here.
def index(request):
    alltask = Tasks.objects.all()
    if request.method == "POST":
        nam = request.POST.get('task')
        desc = request.POST.get('desc')
        user = request.user  
        if nam == "" and desc != "":
            nam = "Next Task"
        if desc == "" and nam != "":
            desc = "Null"
        if desc == "" and nam == "":
            return redirect("/")
        else:
            create_tak = Tasks(user=user,name=nam,desc=desc)
            create_tak.save()
    context = {'alltask':alltask}
    return render(request,'index.html',context)

def delete_confirm(request,pk):
    get_Task = Tasks.objects.get(id=pk)
    context={"get_Task":get_Task}
    return render(request,'defconf.html',context)

def main_del(request,pk):
    get_Task = Tasks.objects.filter(id=pk)
    get_Task.delete()
    return redirect("/")

def clearAll(request):
    user_id = request.user.id
    context ={'user_id':user_id}
    return render(request,'clearall.html',context)


def deleteAll(request,user_id):
    user = User.objects.get(id=user_id)
    get_task = Tasks.objects.filter(user=user)
    get_task.delete()
    return redirect("/")

def sign_up_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        form = User(request.POST)
        if password == password2:
            myuser = User.objects.create_user(username=username,password=password,email=email)
            login(request,myuser)
            return redirect("/")
            myuser.save()
        else:
            return render(request,'signup.html',{'form': form})
    return render(request,'signup.html')

