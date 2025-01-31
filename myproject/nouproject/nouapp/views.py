from django.shortcuts import render,redirect,reverse
from .models import Enquiry, Login, Student
from datetime import date
from django.contrib import messages
from adminapp.models import Program,Branch,Year

# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def registration(request):
    if request.method=="POST":
        rollno=request.POST['rollno']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        program=request.POST['program']
        branch=request.POST['branch']
        year=request.POST['year']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        password=request.POST['password']
        usertype='Student'
        status='false'
        regdate=date.today()
        reg=Student(rollno=rollno, name=name, address=address, fname=fname, mname=mname, gender=gender, program=program, branch=branch, year=year, contactno=contactno, emailaddress=emailaddress, regdate=regdate,)
      
        log=Login(userid=rollno, password=password,usertype=usertype, status=status)
        reg.save()
        log.save()
        messages.success(request,'Registration Completed',locals())
    program=Program.objects.all()
    branch=Branch.objects.all()
    year=Year.objects.all()
    return render(request,'registration.html',locals())

def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        password=request.POST['password']
        try:
            obj=Login.objects.get(userid=userid, password=password)
            if obj.usertype=="Student":
                request.session['rollno']=userid
                return redirect(reverse('studentapp:studenthome'))
            elif obj.usertype=="admin":
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.success(request,'Invalid User')        
    return render(request,'login.html')
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        gender=request.POST['gender']
        address=request.POST['address']
        contactno=request.POST['contactno']
        emailaddress=request.POST['emailaddress']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        enq=Enquiry(name=name, gender=gender, address=address,contactno=contactno, emailaddress=emailaddress, enquirytext=enquirytext, enquirydate=enquirydate )
        enq.save()
        messages.success(request,'Enquiry is submitted')
    return render(request,'contactus.html')