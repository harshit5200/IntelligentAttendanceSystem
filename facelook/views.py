from django.shortcuts import render
from .models import EmployeeModels,live_attendance
from django.http import HttpResponse
import loader
# import weight
import time
import cv2
import os
from datetime import date
from collections import defaultdict
# Create your views here.
def index(request):
    return render(request,'index.html')

def admin2(request):
    return render(request,'admin1.html')

def admin1(request):
    username = request.POST['email']
    password = request.POST['password']

    if "Admin@gmail.com"==username:
        if password=="123456":
            cs=live_attendance.objects.filter(Department="CSE",Date=date.today()).count()
            me=live_attendance.objects.filter(Department="ME",Date=date.today()).count()
            ec=live_attendance.objects.filter(Department="EC",Date=date.today()).count()
            ex=live_attendance.objects.filter(Department="EX",Date=date.today()).count()
            ce=live_attendance.objects.filter(Department="CE",Date=date.today()).count()
            t=cs+me+ec+ex+ce
            mon=live_attendance.objects.values_list('Date')
            jan=0;feb=0;mar=0;apr=0;may=0;jun=0
            for i in mon:
                if i[0][5:7]=='01':
                    jan+=1
                elif i[0][5:7]=='02':
                    feb+=1
                elif i[0][5:7]=='03':
                    mar+=1
                elif i[0][5:7]=='04':
                    apr+=1
                elif i[0][5:7]=='05':
                    may+=1
                elif i[0][5:7]=='06':
                    jun+=1
            context={
                "cse":cs,"me":me,"ec":ec,"ex":ex,"ce":ce,"total":t,"jan":jan,"feb":feb,"mar":mar,"apr":apr,"may":may,"jun":jun
            }
            return render(request ,"file1.html",context)
        else:
            return HttpResponse("<h1>Invalid Password</h1>")
    else:
        return HttpResponse("<h1>UserName is Not Valid</h1>")
    return render(request,"admin1.html")

def emplogin(request):
    return render(request,'emp_login.html')


def emplogin1(request):
    username = request.POST['email']
    globals()['user'] = username
    password = request.POST['password']
    context = dict()
    a=EmployeeModels.objects.all()
    for i in a:
        if i.Mail==username:
            if i.Password==password:
                data=live_attendance.objects.filter(Email=username)
                jan=0;feb=0;mar=0;apr=0;may=0;jun=0
                for j in data:
                    if j.Date[5:7]=='01':
                        jan+=1
                    elif j.Date[5:7]=='02':
                        feb+=1
                    elif j.Date[5:7]=='03':
                        mar+=1
                    elif j.Date[5:7]=='04':
                        apr+=1
                    elif j.Date[5:7]=='05':
                        may+=1
                    elif j.Date[5:7]=='06':
                        jun+=1

                context = {'name':i.Name,'attendance':i.Attendance,'sal':i.Salary,"jan":jan,"feb":feb,"mar":mar,"apr":apr,"may":may,"jun":jun}
                return render(request ,"emplogin.html",context)
            else:
                return HttpResponse("<h1>Invalid Password</h1>")
    else:
        return HttpResponse("<h1>UserName is Not Valid</h1>")
    return render(request,"emp_login.html")

def file1(request):
    cs=live_attendance.objects.filter(Department="CSE",Date=date.today()).count()
    me=live_attendance.objects.filter(Department="ME",Date=date.today()).count()
    ec=live_attendance.objects.filter(Department="EC",Date=date.today()).count()
    ex=live_attendance.objects.filter(Department="EX",Date=date.today()).count()
    ce=live_attendance.objects.filter(Department="CE",Date=date.today()).count()
    t=cs+me+ec+ex+ce
    mon=live_attendance.objects.values_list('Date')
    print(mon)
    jan=0;feb=0;mar=0;apr=0;may=0;jun=0
    for i in mon:
        print(i)
        if i[0][5:7]=='01':
            jan+=1
        elif i[0][5:7]=='02':
            feb+=1
        elif i[0][5:7]=='03':
            mar+=1
        elif i[0][5:7]=='04':
            apr+=1
        elif i[0][5:7]=='05':
            may+=1
        elif i[0][5:7]=='06':
            jun+=1
    context={
        "cse":cs,"me":me,"ec":ec,"ex":ex,"ce":ce,"total":t,"jan":jan,"feb":feb,"mar":mar,"apr":apr,"may":may,"jun":jun
    }
    return render(request,'file1.html',context)


def adduser(request):
    return render(request,'adduser.html')

def live(request):
    import attendance
    name = attendance.final()
    abc=EmployeeModels.objects.all()
    for i in abc:
        if i.Name == name:
            l = live_attendance(Id=i.Id,Name=i.Name,Department = i.Department,Email=i.Mail,Post=i.Post)
            l.save()
            i.Attendance+=1
            i.save()
            break
    c=live_attendance.objects.filter(Date=date.today())
    context={
        'data':c
    }
    return render(request,"liveattend.html",context)


def adduser1(request):
    name = request.POST['name']
    age = request.POST['age']
    dept = request.POST['dept']
    email = request.POST['email']
    pos = request.POST['pos']
    address = request.POST['address']
    city = request.POST['city']
    salary = request.POST['sal']
    e = EmployeeModels(Name=name,Age=age,Department=dept,Mail=email,Post=pos,Address=address,City=city,Salary=salary)
    e.save()
    cam = cv2.VideoCapture(0)

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    count = 0
    directory = name
    parent_dir = 'D:\\Project\\Minor-II\\minor\\images'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path) 
    while(True):
        ret, img = cam.read()
    #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(img, 1.3, 5)
        for (x,y,w,h) in faces:
            x1 = x
            y1 = y
            x2 = x+w
            y2 = y+h
            cv2.rectangle(img, (x1,y1), (x2,y2), (255,255,255), 2)     
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("images/"+name+ "/"+ str(count)+ ".jpg", img[y1:y2,x1:x2])
            cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff
        if k == 27:
            break
        elif count >= 10:
            break
    cam.release()
    cv2.destroyAllWindows()
    return render(request,'adduser.html')

