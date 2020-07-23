from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.

def register(request):

        form = RegisterForm(request.POST or None)
        context ={
                    "form" : form
                              }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
             
            newUser.save()
            login(request,newUser)
            return redirect("index")
                 
        return render(request,"register.html",context)
  
        
def Giris(request):
    form = LoginForm(request.POST or None)

    context = {"form":form}
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user= authenticate(username = username , password  = password)

        if user is None:
                messages.info(request,"Kullanıcı Adı Veya Parola Hatalı")
            
                return render(request,"login.html",context)
        messages.success(request,"Başarıyla giriş yaptınız..")
        login(request,user)
        return redirect("index")
    return render (request,"login.html",context)
        

         
      
             
      
def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")