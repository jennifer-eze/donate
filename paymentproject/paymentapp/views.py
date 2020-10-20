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
    # form = FundForm()
    new_fund = FundForm(request.POST)
    if request.method == 'POST':
        # new_fund = FundForm(request.POST)
        if new_fund.is_valid():
            car_form = new_fund.cleaned_data['name'], new_fund.cleaned_data['fundReason'], new_fund.cleaned_data['image']
            new_fund.save()
        else:
            new_fund = FundForm()
    context = {'car_form':new_fund}
    return render(request, 'paymentapp/startFund.html', context)