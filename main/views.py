from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Offer
from .forms import CreateNewOffer

# Create your views here.


def index(request):
    return render(request, "index.html")

def create(request):
    form = CreateNewOffer()
    return render(request, 'create.html', {"form": form})