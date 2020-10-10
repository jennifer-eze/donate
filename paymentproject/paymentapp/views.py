from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'paymentapp/index.html')

def home(request):
    return render(request, 'paymentapp/home.html')

def startFund(request):
    return render(request, 'paymentapp/startFund.html')