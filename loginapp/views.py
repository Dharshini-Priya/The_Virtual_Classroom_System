from django.shortcuts import redirect, render
from mysql.connector.cursor import SQL_COMMENT
from .models import CourseCreate, User,StuUser,Ass_Create,EX_Create,Submit_Ass,Submit_exam,Ass_Grade,Ex_Grade
import mysql.connector
from operator import itemgetter
from django.contrib import messages


def welcome(req):
    return render(req,'welcome.html')
    
def login(req):
    con = mysql.connector.connect(host = "localhost",user="root",passwd="1234",database="loginsystem")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host = "localhost",user="root",passwd="1234",database="loginsystem")
    cursor2=con2.cursor()
    sqlcommand="select email from loginapp_user"
    sqlcommand2="select password from loginapp_user"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)

    res=list(map(itemgetter(0),e))
    res2=list(map(itemgetter(0),p))

    print(res)
    
    if req.method == "POST":
        email = req.POST['email']
        password = req.POST['password']
        i=1
        k=len(res)
        while i < k:
                   if res[i]==email and res2[i]==password:
                      return render(req,'teacherhome.html',{'email':email})
                      break
                   i+=1
        else:
             messages.info(req,"Check userName or password")
             return redirect('login')
         
    return render(req,'login.html')
    return render(req,'teacherhome.html')  

def register(req):
    if req.method=="POST":
        user = User()

        user.fname=req.POST['fname']
        user.lname=req.POST['lname']
        user.email=req.POST['email']
        user.password=req.POST['password']
        user.cpassword=req.POST['cpassword']
        if user.password != user.cpassword:
            messages.info(req,"Passwords not match")
            return redirect('register')

        elif user.fname=="" or user.lname=="" or user.email=="" or  user.password =="" or user.cpassword=="":
            messages.info(req,'Some fields are missing')
            return redirect('register')

        else:
                messages.info(req,"registration is done go to login")
                user.save()
                return redirect('login')


        
    else:
        return render(req,'register.html')   
            
    

def teacher(req):
    return render(req,'teacher.html')

def teacherhome(req):
    return render(req,'teacherhome.html')
def studenthome(req):
    return render(req,'studenthome.html')


def student(req):
    return render(req,'student.html')

def sturegister(req):
    if req.method=="POST":
        stuuser = StuUser()

        stuuser.fname=req.POST['fname']
        stuuser.lname=req.POST['lname']
        stuuser.roll=req.POST['roll']
        stuuser.email=req.POST['email']
        stuuser.password=req.POST['password']
        stuuser.cpassword=req.POST['cpassword']
        if stuuser.password != stuuser.cpassword:
            messages.info(req,"Passwords not match")
            return redirect('sturegister')

        elif stuuser.fname=="" or stuuser.lname=="" or stuuser.roll==""or stuuser.email=="" or  stuuser.password =="" or stuuser.cpassword=="":
            messages.info(req,'Some fields are missing')
            return redirect('sturegister')

        else:
                messages.info(req,"registration is done !!!")
                stuuser.save()
                return redirect('stulogin') 
    else:
    
          return render(req,'sturegister.html')   
         
def stulogin(req):
    con3 = mysql.connector.connect(host = "localhost",user="root",passwd="1234",database="loginsystem")
    cursor3=con3.cursor()
    con4 = mysql.connector.connect(host = "localhost",user="root",passwd="1234",database="loginsystem")
    cursor4=con4.cursor()
    sqlcommand3="select email from loginapp_stuuser"
    sqlcommand4="select password from loginapp_stuuser"
    cursor3.execute(sqlcommand3)
    cursor4.execute(sqlcommand4)
    e = []
    p = []
    for i in cursor3:
        e.append(i)
    for j in cursor4:
        p.append(j)

    res3=list(map(itemgetter(0),e))
    res4=list(map(itemgetter(0),p))
    
    if req.method == "POST":
        email = req.POST['email']
        password = req.POST['password']
        i=1
        k=len(res3)
        while i < k:
                   if res3[i]==email and res4[i]==password:
                      return render(req,'studenthome.html',{'email':email})
                      break
                   i+=1
        else:
               messages.info(req,"Check userName or password")
               return redirect('stulogin')
         
    return render(req,'stulogin.html')
    return render(req,'studenthome.html') 

def course(req):
    return render(req,'course.html')


def createcourse(req):
    if req.method=="POST":
         createcor = CourseCreate()

         createcor.tname=req.POST['tname']
         createcor.qualification=req.POST['qualification']
         createcor.coursename=req.POST['coursename']
        
        
         if createcor.tname=="" or createcor.coursename=="" or createcor.qualification=="":
            messages.info(req,'Some fields are missing')
            return redirect('createcourse')

         else:
                createcor.save()
                return redirect('course') 
    else:
    
          return render(req,'createcourse.html')   

def coursestu(req):
    key=CourseCreate.objects.all()
    return render(req,'coursestu.html',{'data':key})
    
def coursedetails(req):
    key=CourseCreate.objects.all()
    return render(req,'coursedetails.html',{'data':key})



def ex_home(req):
    return render(req,'ex_home.html')

def ass_home(req):
    return render(req,'ass_home.html')

def ass_create(req):
    if req.method=="POST":
         ass_create = Ass_Create()

         ass_create.cname=req.POST['cname']
         ass_create.topic=req.POST['topic']
         ass_create.question=req.POST['question']
         ass_create.document = req.FILES['document']
         ass_create.time=req.POST['time']
        
        
         if ass_create.cname=="" or ass_create.topic=="" or ass_create.time=="":
            messages.info(req,'Some fields are missing')
            return redirect('ass_create')

         else:
                ass_create.save()
                return redirect('ass_home') 
    else:
    
          return render(req,'ass_create.html')   


def ex_create(req):
    if req.method=="POST":
         createex = EX_Create()

         createex.ename=req.POST['ename']
         createex.topic=req.POST['topic']
         createex.description=req.POST['description']
         createex.document = req.FILES['document']
         createex.time=req.POST['time']
        
         
        
         if createex.ename=="" or createex.topic=="" or  createex.time =="" :
            messages.info(req,'Some fields are missing')
            return redirect('ex_create')

         else:
                createex.save()
                return redirect('ex_home') 
    else:
    
          return render(req,'ex_create.html')

def stu_exam(req):
    key=EX_Create.objects.all()
    return render(req,'stu_exam.html',{'data':key})


def stu_ass(req):
    key=Ass_Create.objects.all()
    return render(req,'stu_ass.html',{'data':key})

def stu_ass_answer(req):
   
    if req.method=="POST":
        submitass = Submit_Ass()

        submitass.name=req.POST['name']
        submitass.roll=req.POST['roll']
        submitass.topic=req.POST['topic']
        submitass.document = req.FILES['document']

       
        if submitass.name=="" or submitass.roll=="" or  submitass.topic =="" :
            messages.info(req,'Some fields are missing')
            return redirect('stu_ass_answer')

        else:
                submitass.save()
                return redirect('stu_ass') 
    else:
        return render(req,'stu_ass_answer.html')

def stu_exam_answer(req):
    if req.method=="POST":
        submitex = Submit_exam()
        submitex.name=req.POST['name']
        submitex.roll=req.POST['roll']
        submitex.topic=req.POST['topic']
        submitex.document = req.FILES['document']
        
        if submitex.name=="" or submitex.roll=="" or  submitex.topic =="" or submitex.document =="":
            messages.info(req,'Some fields are missing')
            return redirect('stu_exam_answer')

        else:
                submitex.save()
                return redirect('stu_exam') 
    else:
        return render(req,'stu_exam_answer.html')

def tea_sub(req):
    return render(req,'tea_sub.html')

def ex_submit(req):
    key=Submit_exam.objects.all()
    return render(req,'ex_submit.html',{'data':key})

def ass_submit(req):
    key=Submit_Ass.objects.all()
    return render(req,'ass_submit.html',{'data':key})

def ass_grade(req):
   
    if req.method=="POST":
        assgrade = Ass_Grade()

        assgrade.roll=req.POST['roll']
        assgrade.cname=req.POST['cname']
        assgrade.obmark=req.POST['obmark']
        assgrade.tomark=req.POST['tomark']
     
       
        if assgrade.cname=="" or assgrade.roll=="" or  assgrade.obmark =="" or assgrade.tomark =="":
            messages.info(req,'Some fields are missing')
            return redirect('ass_grade')

        else:
                assgrade.save()
                return redirect('ass_submit') 
    else:
         return render(req,'ass_grade.html')

def ex_grade(req):
    if req.method=="POST":
        exgrade = Ex_Grade()

        exgrade.cname=req.POST['cname']
        exgrade.roll=req.POST['roll']
        exgrade.obmark=req.POST['obmark']
        exgrade.tomark=req.POST['tomark']
        if exgrade.cname=="" or exgrade.roll=="" or  exgrade.obmark=="" or exgrade.tomark=="" :
            messages.info(req,'Some fields are missing')
            return redirect('ex_grade')

        else:
                exgrade.save()
                return redirect('ex_submit') 
    else:
        return render(req,'ex_grade.html')
def stu_grade(req):
    return render(req,'stu_grade.html')

def stu_ass_grade(req):
    key=Ass_Grade.objects.all()
    return render(req,'stu_ass_grade.html',{'data':key})

def stu_ex_grade(req):
    key=Ex_Grade.objects.all()
    return render(req,'stu_ex_grade.html',{'data':key})
def stu_resource(req):
    return render(req,'stu_resource.html')

def stu_article(req):
    return render(req,'stu_article.html')

def stu_book(req):
    return render(req,'stu_book.html')

def book(req):
    return render(req,'book.html')
    
