from django import forms
from django.forms import ModelForm
from .models import StartFund

class FundForm(ModelForm):
    class Meta():
        model = StartFund
        fields = '__all__'