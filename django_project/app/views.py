from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    # content= {
    #     'name':'Sugam',
    #     'age':23,
    #     'address':'jhapa'
    #      }
    # feature1= Feature()
    # feature1.id =1
    # feature1.name ="Fast"
    # feature1.details="Our services is very fast"

    # feature2= Feature()
    # feature2.id =2
    # feature2.name ="Cost Efficient"
    # feature2.details="Our services is very fast"

    # feature3= Feature()
    # feature3.id =3
    # feature3.name ="Reliable"
    # feature3.details="Our services is very fast"

    # feature4= Feature()
    # feature4.id =4
    # feature4.name ="Quick"
    # feature4.details="Our services is very fast"

    # # feature5= Feature()
    # # feature5.id =5
    # # feature5.name ="Quick"
    # # feature5.details="Our services is very fast"
     
    # features=[feature1,feature2,feature3,feature4]
    features= Feature.objects.all()

    return render(request,'index.html', {'features3' : features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email aleady exist.')
                return redirect('register')
            elif  User.objects.filter(username=username).exists():
                messages.info(request,'Username aleady exist.')
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password dont match')  
            return redirect('register')
    else:
        return render(request,'register.html')

def counter(request):
    text = request.POST['text']
    word_length ={
    'word_lengths' : len(text.split())
    }
    return render(request,'counter.html',word_length)
