from django import forms
from django.forms import ModelForm
from .models import StartFund

class FundForm(ModelForm):
    class Meta():
        model = StartFund
        fields = '__all__'


class DonateForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    amount = forms.IntegerField()