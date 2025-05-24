from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # content= {
    #     'name':'Sugam',
    #     'age':23,
    #     'address':'jhapa'
    #      }
    return render(request,'index.html')

def counter(request):
    text = request.GET['text']
    word_length ={
    'word_lengths' : len(text.split())
    }
    return render(request,'counter.html',word_length)
