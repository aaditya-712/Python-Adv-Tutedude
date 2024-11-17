from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, 'home.html', {'name':'Django'})

def add(request):
    value_1 = int(request.GET['number 1'])
    value_2 = int(request.GET['number 2'])
    res = value_1 + value_2
    return render(request, 'result.html', {'result':res})
