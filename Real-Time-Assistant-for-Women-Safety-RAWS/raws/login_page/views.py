from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from raws import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,"Login/index.html")

def signup(request):
    if request.method == "POST":
        username_reg_back = request.POST.get('username_reg')
        fname_reg_back = request.POST.get('fname_reg')
        lname_reg_back = request.POST.get('lname_reg')
        email1_reg_back = request.POST.get('email1name_reg')
        email2_reg_back = request.POST.get('email2name_reg')
        mobile_reg_back = request.POST.get('mobilename_reg')
        password1_reg_back = request.POST.get('password1_reg')
        password2_reg_back = request.POST.get('password2_reg')

        if User.objects.filter(username = username_reg_back):
            messages.error(request,"Username already exist! Plases try unique value in username")
            return redirect('http://127.0.0.1:8000/login_page/signup')

        if User.objects.filter(email=email1_reg_back):
            messages.error(request,"Email already registered!")
            return redirect('http://127.0.0.1:8000/login_page/signup')

        if len(username_reg_back)>20:
            messages.error(request,"Username must be under 20 characater")
        
        if password1_reg_back != password2_reg_back:
            messages.error(request,"Passwords didn't match!")

        if not username_reg_back.isalnum():
            messages.error(request,"Username must be Alpha-Numeric!")
            return redirect('http://127.0.0.1:8000/login_page/signup')

        myuser = User.objects.create_user(username_reg_back,email1_reg_back,password1_reg_back)
        myuser.first_name = fname_reg_back
        myuser.last_name = lname_reg_back

        myuser.save()

        messages.success(request,"Your Account has been successfull create")

        #Welcome Email
        subject = "Welcome to RAWS (Real-Time Assistant for Women Saftey)"
        message = "Hello "+ myuser.first_name + "!! \n" + "Welcome to RAWS (Real-Time Assistant for Women Saftey) family. Our motive are to provide best saftey for Women. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account.\n\n Thanking You \n RAWS(Real-Time Assistant for Women Saftey)"

        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        return redirect('http://127.0.0.1:8000/login_page/signin')

    return render(request,"Login/signup.html")

def signin(request):
    if request.method == "POST":
        username_back = request.POST.get('username')
        password_back = request.POST.get('password')

        user = authenticate(username=username_back,password=password_back)

        if user is not None:
            fname = user.first_name
            login(request,user)
            return render(request,'Login/home.html',{'fname':fname})
        
        else:
            messages.error(request,"Bad credentionals")
            return redirect('http://127.0.0.1:8000/login_page')

    return render(request,"Login/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return redirect("http://127.0.0.1:8000/login_page/signin")

def location(request):
    return render(request,'Login/location.html')