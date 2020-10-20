from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FundForm
from .models import StartFund

# Create your views here.
def index(request):
    return render(request, 'paymentapp/index.html')

def home(request):
    return render(request, 'paymentapp/home.html')

def startFund(request):
    form = FundForm()
    
    context = {'form':form}
    return render(request, 'paymentapp/startFund.html', context)