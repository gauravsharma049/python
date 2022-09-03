import math
import random
import smtplib


from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')

def SignUp(request):
    users = User.objects.all()
    aotp = 452222
    u=User.objects.filter(otp=aotp)
    digits="0123456789"
    OTP=""
    checkotp = 0
    OTP+=digits[math.floor(random.random()*10)]
    # for i in range(6):
    #     for i in users:
    #         if(i.otp == OTP):
    #             checkotp = 1
    print(u)
    # print(u.username)

    otp = OTP
    msg= otp + " is your OTP"
    em = request.POST.get('Email')
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()

    # s.login("coderstiny65@gmail.com", "sgqjzwfwfvfxcvux")
    print(em)
    if(em != None):
        print(em)
        # s.sendmail('otp verification',em,msg)

    

    
    usercount = 0
    userexist =""
    
    if request.method == 'POST':
            if request.POST.get('Username') and request.POST.get('Mobile_no'):
                user=User()
                for i in users:
                    if(i.username == request.POST.get('Username')):
                        usercount+=1
                        print(i.username)

                if(usercount==0):
                    user.Name= request.POST.get('Name')
                    user.Email= request.POST.get('Email')
                    user.mobile_no= request.POST.get('Mobile_no')
                    user.username= request.POST.get('Username')
                    user.password= request.POST.get('Password')
                    user.otp = otp
                    user.save()
            
                    
                    return redirect('/enterotp')
                else:
                    userexist="username " + request.POST.get('Username')+" already exists"
                    params = {"userExist": userexist}
                    return render(request,'SignUp.html', params)

    else:
            return render(request,'SignUp.html')

def showuser(request):
    users = User.objects.all()
    for i in users:
        print(i.username)
    print(users)
    return render(request, 'formSubmitted.html')

def Login(request):
    name = request.POST.get('Username')
    passw = request.POST.get('Password')
    users = User.objects.all()
    for i in users:
        if(i.username == name and i.password == passw):
            return render(request, 'formSubmitted.html')

    print(users)
    return render(request, 'login.html')

def otpvalidation(request):
    otp = request.POST.get('otp')
    otp_got = True
    print(otp)
    
    # otpgot = User.objects.get(otp=otp)
    # print(otpgot+"hi")
    if(otp !=0 ):
        try: 
            otpgot = User.objects.get(otp=otp)
            print(otpgot)
            otpgot.otp = 0 
            otpgot.save()
            print(otpgot)
    
    
        except:
            otp_got =False

    # otpgot.otp = 123457
    print(otp_got)
    # otpgot.save()
    
    return render(request, 'formSubmitted.html')