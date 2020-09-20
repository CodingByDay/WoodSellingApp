from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Offer
from .forms import CreateNewOffer
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "POST":
        form = CreateNewOffer(request.POST)
        if form.is_valid(): 

            item = form.cleaned_data["item"]  
            quantity1 = form.cleaned_data["quantity1"] 
            second = form.cleaned_data["second"] 
            quantity2 = form.cleaned_data["quantity2"] 
            third = form.cleaned_data["third"] 
            quantity3 = form.cleaned_data["quantity3"] 
            fourth = form.cleaned_data["fourth"] 
            quantity4 = form.cleaned_data["quantity4"] 
            first_last_name = form.cleaned_data["first_last_name"] 
            phone_number = form.cleaned_data["phone_number"] 
            email_address = form.cleaned_data["email_address"] 
            address = form.cleaned_data["address"] 
            t = Offer(item=item,quantity1=quantity1,second=second,quantity2=quantity2,third=third,quantity3=quantity3,fourth=fourth,quantity4=quantity4,first_last_name=first_last_name,phone_number=phone_number,email_address=email_address,address=address)
            t.save()
            messages.success(request, "Uspesno ste napravili ponudu. Na vas email ce stici cena i potvrda.")
            return render(request, 'create.html', {"form": form})
     # RANDOM USEFULL COMMENT            
    else:
       form = CreateNewOffer()
       return render(request, 'create.html', {"form": form})     
   