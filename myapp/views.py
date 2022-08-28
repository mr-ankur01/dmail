from pickle import TRUE
from django.http import FileResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.base import ContentFile
from .fmail import send_forget

from myapp.mailtm import delete
from myapp.models import Inbox ,UserEmail ,ForgetUser
 
#Dmail email
from .mailtm import accounts,toke,msg,files

def inboxMsg(user,address,password):
    token = toke.get_token(address,password)
    msgs = msg.get_msgs(token) 
    try:
        if msgs['hydra:member'] != [] :
            id = msgs['hydra:member'][0]['id']
            res = msg.get_msg(id,token)
            senderEmail = res['from']['address']
            senderName = res['from']['name']
            to = res['to'][0]['address']
            subject = res['subject']
            mailBody = res['html'][0]
            date = res['createdAt']
            if res['attachments'] != []:
                fileName = res['attachments'][0]['filename']
                downloadUrl=res['attachments'][0]['downloadUrl']
                size=res['attachments'][0]['size']
                file = files.get_file(downloadUrl,token)
                file = ContentFile(content=file,name=fileName)
                inbox=Inbox(senderName=senderName,senderEmail=senderEmail,subject=subject,date=date,mailBody=mailBody,to=to,user=user,fileName=fileName,size=size,file=file)
                inbox.save()
                res = delete.delete_msg(id,token)
                print(res)
                return True
            inbox=Inbox(senderName=senderName,senderEmail=senderEmail,subject=subject,date=date,mailBody=mailBody,to=to,user=user)
            inbox.save()
            res = delete.delete_msg(id,token)
            print(res)
            return True
    except Exception as e:
        print('inboxMsg',e)
               
# Create your views here.
def home(request):
    if request.user.id:  
        inbox_info=Inbox.objects.filter(user=request.user.id)
        user=UserEmail.objects.filter(user=request.user.id).first()
        address = user.address 
        password = user.password 
        user = request.user 
        inboxMsg(user,address,password)
        context  ={
            'inbox':inbox_info,
            'email':address
        }    
        return render(request,'app/home.html',context)
    else:
        user_id =None
        inbox_info=Inbox.objects.filter(user=user_id)
        user=UserEmail.objects.filter(user=user_id).first()
        try:
            address = user.address 
            password = user.password  
        except:
            from .mailtm import generate_address,generate_password,domain
            address = generate_address() + domain
            password = generate_password() 
            print(address)
            UserEmail.objects.filter(user=user_id).delete()
            acc = accounts.create(address,password)
            print(acc)
            acc_id=acc['id']
            mail=UserEmail(address=address,password=password,user=user,acc_id=acc_id)
            mail.save()
        inboxMsg(user_id,address,password)
        context  ={
            'inbox':inbox_info,
            'email':address,
        } 
    
        return render(request,'app/home.html',context)

def change(request):
    if request.user.id:
        user = request.user
    else:
        user = None
    umail = UserEmail.objects.filter(user=user).first()
    address=umail.address
    passsword=umail.password
    id=umail.acc_id
    token = toke.get_token(address,passsword)
    del_acc= accounts.delete(id,token)
    print(del_acc)
    from .mailtm import generate_address,generate_password,domain
    address = generate_address() + domain
    password = generate_password() 
    UserEmail.objects.filter(user=user).delete()
    acc = accounts.create(address,password)
    acc_id=acc['id']
    mail=UserEmail(address=address,password=password,user=user,acc_id=acc_id)
    mail.save()
    return redirect('/')

def message(request,id):
    inbox_info=Inbox.objects.filter(id=id).first()
    context={
        'inbox':inbox_info
    }
    return render(request,'app/msg.html',context)

def download(request,id):
    inbox_info=Inbox.objects.filter(id=id).first()
    file=inbox_info.file
    filename=inbox_info.fileName
    return FileResponse(file,as_attachment=TRUE ,filename=filename)

def delmsg(request,id):
    Inbox.objects.filter(id=id).delete()
    return redirect('/')

@login_required
def custom(request):
    if request.method == 'POST':
        custom_addr = request.POST.get('email')
        if len(custom_addr) < 4 or len(custom_addr) >= 20 :
            messages.error(request,'Error! Email must be between 4 and 20 character!')
        elif any(x.isupper() for x in custom_addr):
            messages.error(request,'Error! Address should be in lower case letter')
        else:
            user = request.user
            umail = UserEmail.objects.filter(user=user).first()
            address=umail.address
            password=umail.password
            address1=umail.address
            password2=umail.password
            id=umail.acc_id
            token = toke.get_token(address,password)
            del_acc= accounts.delete(id,token)
            print(del_acc)
            from .mailtm import password,domain
            acc = accounts.create(custom_addr+domain,password)
            try:
                acc_id=acc['id']
            except:
                acc = accounts.create(address1,password2)
                messages.error(request,'Account has already created')
                return render(request,'custom.html')
            else:
                UserEmail.objects.filter(user=user).delete()
                mail=UserEmail(address=custom_addr+domain,password=password,user=user,acc_id=acc_id)
                mail.save()
                return redirect('/')
    return render(request,'app/custom.html')

def sign(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request,'Error! Confirm Password Not Match')
        elif len(password1) < 4 or len(password1) >= 10 :
            messages.error(request,'Error! Password must be between 4 and 10 character!')
        else:
            user = User.objects.filter(username=email).first()
            if user:
                messages.error(request,'Account already exists ')
                return redirect('/login')
            else: 
                user = User.objects.create_user(email,email,password1)
                from .mailtm import accounts,address,password
                try:
                    acc = accounts.create(address,password)
                    print(acc)
                    acc_id=acc['id']
                except:
                    from .mailtm import accounts,generate_address,generate_password,domain
                    address=generate_address() + domain
                    password=generate_password()
                    acc = accounts.create(address,password)
                    print(acc)
                    acc_id=acc['id']
                user.save()
                mail=UserEmail(address=address,password=password,user=user,acc_id=acc_id)
                mail.save()
                messages.success(request,'Your account successfully created')
                return redirect('/login')
    return render(request,'registration/sign.html')

def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.filter(username=email).first()
        if username is None:
            messages.error(request,'Email Not Found Please create an Account')
        else:  
            user = authenticate(request,username = email,password = password)
            if user is not None:
                login(request, user)
                return redirect('/') 
            else:
                messages.error(request,'Password is wrong') 
    return render(request,'registration/login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/login')

def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not User.objects.filter(username = email).first() :
            messages.error(request,'Email Not Found')
        else:
            import uuid
            user_obj = User.objects.get(username = email)
            token = str(uuid.uuid4())
            delfuser = ForgetUser.objects.filter(user = user_obj)
            if delfuser:
                delfuser.delete()
            fuser = ForgetUser(user = user_obj,token = token)
            fuser.save()
            send_forget(email,token)
            messages.success(request,'An email is sent , check your mailbox')
    
    return render(request,'registration/forget.html')


def changePass(request,token):
    fuser = ForgetUser.objects.filter(token=token).first()
    user_id = fuser.user.id
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if user_id is None:
            messages.error(request,'no user found')
            return redirect(f'/change-pass/{token}')
        
        if password1 != password2:
            messages.error(request,'Error! Confirm Password Not Match')
            
        elif len(password1) < 4 or len(password1) >= 10 :
            messages.error(request,'Error! Password must be between 4 and 10 character!') 
            
        else:
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(password1)
            user_obj.save()
            messages.success(request,'Password is changed successfully')
            return redirect('/login')
             
    
    return render(request,'registration/change_pass.html')

def docs(request):
    return render(request,'app/docs.html')


def ex(request):
    return render(request,'app/ex.html')
