from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from student_managment_system.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .models import Events
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def custom_404(request, exception):
    return render(request, '404.html', status=404)



def showloginPage(request):
    return render(request,"SingUp.html")








def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:

        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                messages.success(request, "تم تسجيل الدخول بنجاح !")
                return HttpResponseRedirect('/')
            elif user.user_type=="2":
                messages.success(request, "Login successful.")
                return HttpResponseRedirect(('/'))
            else:
                return HttpResponseRedirect(('/'))
        else:
            messages.error(request,"عفوا  اسم المستخدم او كلمة المرور غير صحيحة")
            return HttpResponseRedirect('/')

def GetUserDetails(request):
    if request.user!=None:
       return HttpResponse ("User :" +request.user.email+"usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("please login frist")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')




from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_password_reset_email(user_email, reset_url):
    subject = 'Password Reset - ST-Mrak-School'
    html_message = render_to_string('password_reset_email.html', {'protocol': 'http', 'domain': 'example.com', 'uid': '123', 'token': 'abc123', 'user_name': 'John Doe'})
    plain_message = strip_tags(html_message)  # This removes the HTML tags for the plain text version
    from_email = 'your@example.com'
    to_email = user_email

    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
