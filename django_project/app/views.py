from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

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

def counter(request):
    text = request.POST['text']
    word_length ={
    'word_lengths' : len(text.split())
    }
    return render(request,'counter.html',word_length)
