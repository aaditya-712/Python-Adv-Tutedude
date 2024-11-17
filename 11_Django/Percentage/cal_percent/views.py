from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return render(request, 'home.html', {'name':'Enter marks'})

def calculate(request):
    eng = int(request.GET['english'])
    mar = int(request.GET['marathi'])
    hin = int(request.GET['hindi'])
    math = int(request.GET['maths'])
    sci = int(request.GET['science'])
    total = eng + mar + hin + math + sci
    percentage = (total * 100) / 500
    return render(request, 'result.html', {'percent':percentage,'total':total})