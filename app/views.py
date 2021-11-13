from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
   
    print("hi i am bored.")
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']
        print(subject)
        print('this is awesome')
        send_mail(
            subject ,
            message,
            settings.EMAIL_HOST_USER,
            [email])
    return render(request , 'app/home.html')
def success(request):
    return render(request , 'app/success.html')


    

       
    

    
