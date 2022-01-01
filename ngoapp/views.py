from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.
def index(request):

    coverdata = homecover.objects.all()[0]
    causedata = ourcause.objects.all()
    teamdata = team.objects.all()
    galldata = gallary.objects.all()[0:8]

    dat = eventss.objects.all()[0:4]
    hddata = heading1.objects.all()[0]
    hddataa = heading2.objects.all()[0]
    vol1 =volunteerimage.objects.all()[0]
    volunteerimage
    context = {
    'coverx': coverdata,
    'cau': causedata,
    'team': teamdata,
    'gal': galldata,

    'dat':dat,
    'hde': hddata,
    'hdee': hddataa,
    'vol1':vol1

    }
    return render(request,'index.html',context)

def about(request):
    teamdata = team.objects.all()
    hddata = heading1.objects.all()[0]
    coverdata = aboutcover.objects.all()[0]
    context = {
    'coverx': coverdata,
    'team': teamdata,
    'hde': hddata,
    }
    return render(request,'about.html',context)

def blogsingle(request):
    return render(request,'blog-single.html')

def contact(request):
    cont = contactinfo.objects.all()[0]
    ct=contactuscover.objects.all()[0]
    context = {
    'cont': cont,
    'ct':ct,
    }
    return render(request,'contact.html',context)

def donate(request):
    vol1 =volunteerimage.objects.all()[0]
    teamdata = donateteam.objects.all()
    don = donatecover.objects.all()[0]
    context = {
    'don': don,
    'team': teamdata,
    'vol1':vol1
    }
    return render(request,'donate.html',context)

def event(request):
    dat = eventss.objects.all()
    ev = eventcover.objects.all()[0]
    context = {
    'ev': ev,
    'dat':dat,
    }
    return render(request,'event.html',context)

def cause(request):
    vol1 =volunteerimage.objects.all()[0]
    causedata = ourcause.objects.all()
    cata = causecover.objects.all()[0]
    context={
    'cau': causedata,
    'cata': cata,
    'vol1':vol1


    }
    return render(request,'causes.html',context)

def blog(request):
    return render(request,'blog.html')

def gallery(request):
    vol1 =volunteerimage.objects.all()[0]
    galldata = gallary.objects.all()
    galc = gallerycover.objects.all()[0]
    context={
    'galc':galc,
    'gal': galldata,
    'vol1':vol1}
    return render(request,'gallery.html',context)

def send_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        data =contactxform(name=name,email=email,phone=phone,message=message)
        data.save()
        return redirect('index')
    else:
        return redirect('index')

def query_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        data =contactxqueryform(name=name,email=email,phone=phone,subject=subject,message=message)
        data.save()
        return redirect('contact')
    else:
        return redirect('contact')

def volregister(request):

    ct=volregistercover.objects.all()[0]
    context ={
    'ct':ct,}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']


        if password == password1:
            if volunterregisterform.objects.filter(username=username).exists():
                print("Username already used")
                return redirect("volregister")

            elif volunterregisterform.objects.filter(email=email).exists():
                print("Email already used")
                return redirect("volregister")

            else:
                var = volunterregisterform(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                var.save()
                return redirect('event')
        else:
            print("password doesnt match")
            return redirect("volregister")

    return render(request,'volregister.html',context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')

        else:
             messages.error(request, 'Your password or username invalid')
             return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password1 = request.POST['password2']


        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect("register")

            elif User.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
                return redirect("register")

            else:
                var = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                var.save()
                return redirect('login')
        else:
            messages.error(request,'password and confirm_password not matched')
            return redirect("register")

    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    messages.success(request, 'You logout successfully')
    return redirect('login')

def changepassword(request):
    if request.method == 'POST':
        fm=PasswordChangeForm(user=request.user,data=request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('index')
        else:
            return redirect('changepassword')
    else:
        fm=PasswordChangeForm(user=request.user)
    return render(request,'changepass.html',{'fm':fm})
