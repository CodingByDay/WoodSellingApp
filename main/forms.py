from django import forms
from .models import Item, Offer





class CreateNewOffer(forms.Form):

    # Item information.

    item = forms.ModelChoiceField(queryset=Item.objects.all(), label="Prvi artikal.")
    quantity1 = forms.IntegerField(label="Količina.", required=False)               
    second = forms.ModelChoiceField(queryset=Item.objects.all(), label="Drugi artikal.",required=False)                     
    quantity2 = forms.IntegerField(label="Količina.",required=False)                     
    third = forms.ModelChoiceField(queryset=Item.objects.all(), label="Treći artikal.",required=False)                      
    quantity3 = forms.IntegerField(label="Količina.",required=False)                  
    fourth = forms.ModelChoiceField(queryset=Item.objects.all(), label="Četvrti artikal.",required=False)                     
    quantity4 = forms.IntegerField(label="Količina.",required=False)  
    # Contact information.    
    # User info.                
    first_last_name =forms.CharField(label="Ime i prezime", max_length = 200)            
    phone_number =   forms.IntegerField(label="Broj telefona")          
    email_address = forms.EmailField(label="Email adresa.")           
    address = forms.CharField(label="Adresa za dostavu.", max_length = 200)                      
                     
                       