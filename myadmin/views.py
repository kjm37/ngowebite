from django.shortcuts import render,redirect
from ngoapp.models import *
# Create your views here.




def admingallaryx(request):
    galldata = gallary.objects.all()
    context={
    'gal': galldata,
    }
    return render(request,'admingallary/admingallary.html',context)

def vadmingallaryx(request):
    xcx= volunteerimage.objects.all()
    context={
    'gal': xcx,
    }
    return render(request,'volunteerimagecover/vadmingallary.html',context)


def hadmingallaryx(request):
    hgalldata = homecover.objects.all()
    context={
    'gall': hgalldata,
    }
    return render(request,'homecover/hadmingallary.html',context)


def aadmingallaryx(request):
    agalldata = aboutcover.objects.all()
    context={
    'gal': agalldata,
    }
    return render(request,'aboutcover/aadmingallary.html',context)

def dadmingallaryx(request):
    done = donatecover.objects.all()
    context={
    'gal': done,
    }
    return render(request,'donatecover/dadmingallary.html',context)

def cadmingallaryx(request):
    dk =causecover.objects.all()
    context={
    'gal': dk,
    }
    return render(request,'causecover/cadmingallary.html',context)


def eadmingallaryx(request):
    edata = eventcover.objects.all()
    context={
    'gal':edata,
    }
    return render(request,'eventcover/eadmingallary.html',context)

def gadmingallaryx(request):
    gg = gallerycover.objects.all()
    context={
    'gal':gg,
    }
    return render(request,'gallerycover/gadmingallary.html',context)

def uadmingallaryx(request):
    zz = contactuscover.objects.all()
    context={
    'gal':zz,
    }
    return render(request,'contactuscover/uadmingallary.html',context)

def cfadmingallaryx(request):
    ff = contactxform.objects.all()
    context={
    'gal':ff,
    }
    return render(request,'contactxform/cfadmingallary.html',context)


def ciadmingallaryx(request):
    att = contactinfo.objects.all()
    context={
    'gal':att,
    }
    return render(request,'contactinfo/ciadmingallary.html',context)

def ccfadmingallaryx(request):
    tt = contactxqueryform.objects.all()
    context={
    'gal':tt,
    }
    return render(request,'contactxqueryform/ccfadmingallary.html',context)


def add_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        image=gallary(image=img,title=name)
        image.save()
        return redirect('admingallary')
    else:
        return render(request,'admingallary/add-gallary.html')


def vadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        image=volunteerimage(image=img,title=name)
        image.save()
        return redirect('vadmingallary')
    else:
        return render(request,'volunteerimagecover/vadd-gallary.html')



def  hadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=homecover(image=img,title=name,description=description)
        image.save()
        return redirect('hadmingallary')
    else:
        return render(request,'homecover/hadd-gallary.html')

def aadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=aboutcover(image=img,title=name,description=description)
        image.save()
        return redirect('aadmingallary')
    else:
        return render(request,'aboutcover/aadd-gallary.html')

def dadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=donatecover(image=img,title=name,description=description)
        image.save()
        return redirect('dadmingallary')
    else:
        return render(request,'donatecover/dadd-gallary.html')

def cadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=causecover(image=img,title=name,description=description)
        image.save()
        return redirect('cadmingallary')
    else:
        return render(request,'causecover/cadd-gallary.html')

def eadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=eventcover(image=img,title=name,description=description)
        image.save()
        return redirect('eadmingallary')
    else:
        return render(request,'eventcover/eadd-gallary.html')

def gadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=gallerycover(image=img,title=name,description=description)
        image.save()
        return redirect('gadmingallary')
    else:
        return render(request,'gallerycover/gadd-gallary.html')

def cfadd_image(request):
    user=request.user
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        cox=contactxform(name=name,email=email,phone=phone,message=message)
        cox.save()
        return redirect('cfadmingallary')
    else:
        return render(request,'contactxform/cfadd-gallary.html')

def ciadd_image(request):
    user=request.user
    if request.method == 'POST':
        address=request.POST['address']
        email=request.POST['email']
        mobile=request.POST['mobile']
        website=request.POST['website']
        cox=contactinfo(address=address,email=email,mobile=mobile,website=website)
        cox.save()
        return redirect('ciadmingallary')
    else:
        return render(request,'contactinfo/ciadd-gallary.html')


def ccfadd_image(request):
    user=request.user
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        cox=contactxqueryform(name=name,email=email,subject=subject,phone=phone,message=message)
        cox.save()
        return redirect('ccfadmingallary')
    else:
        return render(request,'contactxqueryform/ccfadd-gallary.html')



def uadd_image(request):
    user=request.user
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        image=contactuscover(image=img,title=name,description=description)
        image.save()
        return redirect('uadmingallary')
    else:
        return render(request,'contactuscover/uadd-gallary.html')


def del_galary(request,id):
    img=gallary.objects.get(id=id)
    img.delete()
    return redirect('admingallary')

def vdel_galary(request,id):
    img=volunteerimage.objects.get(id=id)
    img.delete()
    return redirect('vadmingallary')


def hdel_galary(request,id):
    img=homecover.objects.get(id=id)
    img.delete()
    return redirect('hadmingallary')

def adel_galary(request,id):
    img=aboutcover.objects.get(id=id)
    img.delete()
    return redirect('aadmingallary')

def ddel_galary(request,id):
    img=donatecover.objects.get(id=id)
    img.delete()
    return redirect('dadmingallary')


def cdel_galary(request,id):
    img=causecover.objects.get(id=id)
    img.delete()
    return redirect('cadmingallary')


def edel_galary(request,id):
    img=eventcover.objects.get(id=id)
    img.delete()
    return redirect('eadmingallary')

def gdel_galary(request,id):
    img=gallerycover.objects.get(id=id)
    img.delete()
    return redirect('gadmingallary')


def udel_galary(request,id):
    img=contactuscover.objects.get(id=id)
    img.delete()
    return redirect('uadmingallary')


def cfdel_galary(request,id):
    img=contactxform.objects.get(id=id)
    img.delete()
    return redirect('cfadmingallary')


def cidel_galary(request,id):
    img=contactinfo.objects.get(id=id)
    img.delete()
    return redirect('ciadmingallary')


def ccfdel_galary(request,id):
    img=contactxqueryform.objects.get(id=id)
    img.delete()
    return redirect('ccfadmingallary')


def updat(request,id):
    da=gallary.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        data=gallary(id=id,image=img,title=name)
        data.save()
        return redirect('admingallary')
    else:
        return render(request,'admingallary/admupdate.html',{'da':da})

def vupdat(request,id):
    dii=volunteerimage.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        data=volunteerimage(id=id,image=img,title=name)
        data.save()
        return redirect('vadmingallary')
    else:
        return render(request,'volunteerimagecover/vadmupdate.html',{'da':dii})




def hupdat(request,id):
    zdata=homecover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        udata=homecover(id=id,image=img,title=name,description=description)
        udata.save()
        return redirect('hadmingallary')
    else:
        return render(request,'homecover/hadmupdate.html',{'zd':zdata})


def aupdat(request,id):
    da=aboutcover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        data=aboutcover(id=id,image=img,title=name,description=description)
        data.save()
        return redirect('aadmingallary')
    else:
        return render(request,'aboutcover/aadmupdate.html',{'da':da})

def dupdat(request,id):
    op=donatecover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        op=donatecover(id=id,image=img,title=name,description=description)
        op.save()
        return redirect('dadmingallary')
    else:
        return render(request,'donatecover/dadmupdate.html',{'dae':op})




def cupdat(request,id):
    cat=causecover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        cat=causecover(id=id,image=img,title=name,description=description)
        cat.save()
        return redirect('cadmingallary')
    else:
        return render(request,'causecover/cadmupdate.html',{'dae':cat})



def eupdat(request,id):
    ee=eventcover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        cat=eventcover(id=id,image=img,title=name,description=description)
        cat.save()
        return redirect('eadmingallary')
    else:
        return render(request,'eventcover/eadmupdate.html',{'dae':ee})

def gupdat(request,id):
    ii=gallerycover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        cat=gallerycover(id=id,image=img,title=name,description=description)
        cat.save()
        return redirect('gadmingallary')
    else:
        return render(request,'gallerycover/gadmupdate.html',{'dae':ii})

def uupdat(request,id):
    ij=contactuscover.objects.get(id=id)
    if request.method == 'POST':
        img=request.FILES['pic']
        name=request.POST['title']
        description=request.POST['description']
        ij=contactuscover(id=id,image=img,title=name,description=description)
        ij.save()
        return redirect('uadmingallary')
    else:
        return render(request,'contactuscover/uadmupdate.html',{'dae':ij})


def cfupdat(request,id):
    dx=contactxform.objects.get(id=id)
    context = {'dx': dx}

    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        cox=contactxform(id=id,name=name,email=email,phone=phone,message=message)
        cox.save()
        return redirect('cfadmingallary')

    return render(request,'contactxform/cfadmupdate.html',context)


def ciupdat(request,id):
    bu=contactinfo.objects.get(id=id)
    context = {'dx': bu}

    if request.method == 'POST':
        address=request.POST['address']
        email=request.POST['email']
        mobile=request.POST['mobile']
        website=request.POST['website']
        bu=contactinfo(id=id,address=address,email=email,mobile=mobile,website=website)
        bu.save()
        return redirect('ciadmingallary')

    return render(request,'contactinfo/ciadmupdate.html',context)





def ccfupdat(request,id):
    dxx=contactxqueryform.objects.get(id=id)
    context = {'dx': dxx}

    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        cox=contactxqueryform(id=id,name=name,email=email,subject=subject,phone=phone,message=message)
        cox.save()
        return redirect('ccfadmingallary')

    return render(request,'contactxqueryform/ccfadmupdate.html',context)


def title(request):
    hddata = heading1.objects.all()
    context = {'hde': hddata}
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']

        var=heading1(title=title,description=description)
        var.save()
        return redirect('title')
    else:
        return render(request,'adminhd/headingtitle.html',context)

def title2(request):
    hddata2 = heading2.objects.all()
    context = {'hde': hddata2}
    if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']

        var=heading2(title=title,description=description)
        var.save()
        return redirect('title2')
    else:
        return render(request,'adminhd2/headingtitle2.html',context)


def hd(request):
    return render(request,'adminhd/inputhd.html')

def hd2(request):
    return render(request,'adminhd2/inputhd2.html')

def hde(request,id):
    data=heading1.objects.get(id=id)
    data.delete()
    return redirect('title')

def hde2(request,id):
    data2=heading2.objects.get(id=id)
    data2.delete()
    return redirect('title2')

def titleupdat(request,id):
    hddata = heading1.objects.get(id=id)
    context = {'hde': hddata}
    if request.method == 'POST':
        titlex=request.POST['title']
        descriptionx=request.POST['description']

        hddata=heading1(id=id,title=titlex,description=descriptionx)
        hddata.save()
        return redirect('title')
    else:
        return render(request,'adminhd/uptitle.html',context)

def titleupdat2(request,id):
    hddata2 = heading2.objects.get(id=id)
    context = {'hde': hddata2}
    if request.method == 'POST':
        titlex=request.POST['title']
        descriptionx=request.POST['description']

        hddata=heading2(id=id,title=titlex,description=descriptionx)
        hddata.save()
        return redirect('title2')
    else:
        return render(request,'adminhd2/uptitle2.html',context)

def our(request):
    causedata = ourcause.objects.all()
    context = {'cau': causedata,}
    if request.method == 'POST':
        img=request.FILES['pic']
        title=request.POST['title']
        description=request.POST['description']

        var=ourcause(image=img,title=title,description=description)
        var.save()
        return redirect('our')

    return render(request,'ourcausem/our.html',context)

def ourdel(request,id):
    data=ourcause.objects.get(id=id)
    data.delete()
    return redirect('our')


def addcause(request):
    return render(request, 'ourcausem/addcause.html')

def upour(request,id):
    causedata = ourcause.objects.get(id=id)
    context = {'cau': causedata}

    if request.method == 'POST':
        img=request.FILES['pic']
        titlex=request.POST['title']
        descriptionx=request.POST['description']

        var=ourcause(id=id,image=img,title=titlex,description=descriptionx)
        var.save()
        return redirect('our')

    return render(request,'ourcausem/upour.html',context)


def displayevent(request):
    x = eventss.objects.all()
    context = {'x': x}
    if request.method == 'POST':
        img=request.FILES['pic']
        eventname=request.POST['eventname']
        cityname=request.POST['cityname']
        address=request.POST['address']
        date=request.POST['date']
        var=eventss(image=img,eventname=eventname,cityname=cityname,address=address,date=date)
        var.save()
        return redirect('ent')

    return render(request,'events/displayevent.html',context)

def addevents(request):
    return render(request, 'events/addevents.html')

def eventdel(request,id):
    data=eventss.objects.get(id=id)
    data.delete()
    return redirect('ent')

def upevent(request,id):
    x = eventss.objects.get(id=id)
    context = {'x': x}
    if request.method == 'POST':
        img=request.FILES['pic']
        eventname=request.POST['eventname']
        cityname=request.POST['cityname']
        address=request.POST['address']
        date=request.POST['date']
        var=eventss(id=id,image=img,eventname=eventname,cityname=cityname,address=address,date=date)
        var.save()
        return redirect('ent')

    return render(request,'events/upevent.html',context)



def displayteam(request):
    x = team.objects.all()
    context = {'x': x}
    if request.method == 'POST':
        img=request.FILES['pic']
        title=request.POST['title']
        description=request.POST['description']

        var=team(image=img,title=title,description=description)
        var.save()
        return redirect('disteam')

    return render(request, 'team/displayteam.html', context)


def addteam(request):
    return render(request, 'team/addteam.html')


def teamdel(request,id):
    data=team.objects.get(id=id)
    data.delete()
    return redirect('disteam')

def upteam(request,id):
    x = team.objects.get(id=id)
    context = {'x': x}
    if request.method == 'POST':
        img=request.FILES['pic']
        titlex=request.POST['title']
        descriptionx=request.POST['description']

        var=team(id=id,image=img,title=titlex,description=descriptionx)
        var.save()
        return redirect('disteam')

    return render(request,'team/upteam.html',context)


def donateteamm(request):
    xa=donateteam.objects.all()
    context = {'xa': xa}
    if request.method == 'POST':
        img=request.FILES['pic']
        title=request.POST['title']
        description=request.POST['description']

        var=donateteam(image=img,title=title,description=description)
        var.save()
        return redirect('donateteam')

    return render(request,'donate/donateteam.html',context)

def dondel(request,id):
    ya=donateteam.objects.get(id=id)
    ya.delete()
    return redirect('donateteam')

def adddteam(request):

    return render(request,'donate/adddonateteam.html')

def donupteam(request,id):
    xw = donateteam.objects.get(id=id)
    context = {'xw': xw}
    if request.method == 'POST':
        img=request.FILES['pic']
        titlex=request.POST['title']
        descriptionx=request.POST['description']

        var=donateteam(id=id,image=img,title=titlex,description=descriptionx)
        var.save()
        return redirect('donateteam')

    return render(request,'donate/donupteam.html',context)
