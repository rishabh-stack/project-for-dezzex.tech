from django.shortcuts import render,redirect,HttpResponse
from.models import signUp
from django.contrib import messages

# Create your views here.
def handleSignup(request):
    if request.method=='POST':
        # Get the post parameters
        fullname=request.POST['name']
        email =request.POST['email']
        phone =request.POST['phone']
        passp =request.POST['passp']
        birthday =request.POST['birthday']
        img =request.POST['img']
        password=request.POST['password']
        data=signUp(fullname=fullname,email=email,phone=phone,passp=passp,dob=birthday,img=img,password=password)
        data.save()
        messages.success(request,'Your account has been created successfully')
        return redirect('/')

def handlelogIn(request):
    query1=request.POST.get('uname')
    query2=request.POST.get('psw')
     
    #         return render(request,"login.html",dic)
    #     else:
    #         messages.error(request,'User not found')
    #         return redirect('/')
    check = signUp.objects.filter(phone=query1, password=query2)
    
    
    if len(check)>0 :
        fr=signUp.objects.all().filter(phone=query1)
        # for item in catprods:
    #     if query1 in item.phone and query2 in item.phone:
        dic={"product":fr[0]}
        # update = signUp.objects.filter(phone=query1)
        # product = []
        # for item in update:
        #     product.append({'fullname': item.fullname, 'email': (item.email),'phone': (item.phone),'passp': (item.passp),'dob': (item.dob),'img': (item.img)})
        
        # print(product)
        # dic={"product":product[0]}  
        messages.success(request,'you have successfully logged in Dezzex.in')
        return render(request,"login.html",dic)
    else:
        messages.error(request,'User not found')
        return redirect('/')
       
def handlelogOut(request):
    messages.success(request,'you have successfully logged out')
    return render(request,"index2.html")

def index(request):
    return render(request,"index2.html")