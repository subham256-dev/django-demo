from django.shortcuts import render,redirect
from .models import * 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
    
        Receipe.objects.create(
             receipe_name=receipe_name,
             receipe_description=receipe_description,
             receipe_image=receipe_image

        )
       
        return redirect ('/receipes/')

    queryset=Receipe.objects.all()

    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(receipe_name__icontains=search)




    context={'receipe':queryset}
    

    return render (request,'receipes.html',context)


def delete_receipe(request,id):
        receipe=Receipe.objects.get(id=id)
        receipe.delete()
        return redirect('/receipes/')
    
    

def update_receipe(request,id):
    receipe=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
    
        receipe.receipe_name=receipe_name
        receipe.receipe_description=receipe_description
        if receipe_image:
            receipe.receipe_image=receipe_image

        receipe.save()
        return redirect ('/receipes/')
    context={'receipe':receipe}
    return render(request,'update_receipe.html',context)



def login_page(request):
    if request.method=="POST":
       username=request.POST.get('username')
       password=request.POST.get('password')

       if not User.objects.filter(username=username).exists():
           messages.info(request,"Invalid username ")
           return redirect('/login/')
       user=authenticate(username=username,password=password)
       if user is None:
           messages.info(request,"Invalid password ")
           return redirect('/login/')

       else:
            login(request,user)
            return redirect('/receipes/')

    return render(request,'login.html')





def register_page(request):
    if request.method=="POST":
       username=request.POST.get('username')
       fist_name=request.POST.get('first_name')
       last_name=request.POST.get('last_name') 
       password=request.POST.get('password')


       if User.objects.filter(username=username).exists():
        messages.info(request,"Username already exists")
        return redirect('/register/')
           

       user=User.objects.create(username=username, first_name=fist_name, last_name=last_name, )
       user.set_password(password)
       user.save()
       messages.info(request,"User created successfully")
       return redirect('/register/')


    return render(request,'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')