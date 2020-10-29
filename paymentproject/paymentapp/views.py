from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
from .forms import FundForm, DonateForm
from .models import StartFund

import stripe
# Fill in your api key
stripe.api_key = ""

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
    form = DonateForm()
    return render(request, 'paymentapp/donate.html', {'form':form})
    # return render(request, 'paymentapp/donate.html')

def charge(request):
    
    if request.method == 'POST':
        print('Data:',request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            name=request.POST['name'],
            email=request.POST['email'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='eur',
            description="Donation"
        )

    return redirect(reverse('success', args=[amount]))

def successMassage(request, args):
    amount = args
    return render(request, 'paymentapp/success.html', {'amount':amount})