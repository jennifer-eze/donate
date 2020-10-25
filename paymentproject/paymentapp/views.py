from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import FundForm, DonateForm
from .models import StartFund

import stripe

stripe.api_key = "sk_test_51HfjeECnG9zuAAzuS44E1KDe89nOdbhcO0vDUxwBnsBrTxPipa3Jq0jYYTMvYpwomoHPtQS7a826WH155ttFTOeh00W4xm1nxV"

# Create your views here.
def index(request):
    return render(request, 'paymentapp/index.html')

def home(request):
    allFunds = StartFund.objects.all()
    
    return render(request, 'paymentapp/home.html', {'allFunds':allFunds})

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

def donate(request):
    # form = DonateForm()
    # return render(request, 'paymentapp/donate.html', {'form':form})
    return render(request, 'paymentapp/donate.html')