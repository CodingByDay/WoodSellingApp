from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
#
#
#
STOCK_CHOICES = ( 
    ("1", "Da."), 
    ("2", "Ne."), 
   
) 

class Item(models.Model):
    ime                         =models.CharField(max_length=150)
    opis                  =models.CharField(max_length=200)
    cena                       =models.IntegerField()
    lager = models.CharField(

        max_length = 20, 
        choices = STOCK_CHOICES, 
        default = '1'

        ) 

    def __str__(self):
        return self.ime


######################################################################################
class Offer(models.Model):
    item                         =models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity1                     =models.IntegerField(null=False)   
    second                       =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='second', null=True)
    quantity2                     =models.IntegerField(null=True)
    third                        =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='third', null=True)
    quantity3                    =models.IntegerField(null=True)
    fourth                       =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='fourth', null=True)
    quantity4                     =models.IntegerField(null=True)
    first_last_name              =models.CharField(max_length=120)
     
    phone_number                 =models.IntegerField() 
    email_address                =models.EmailField(null=False)   
    address                      =models.CharField(max_length=120)
    datetime                     =models.DateTimeField()
    finalOffer                   =models.IntegerField()
    sendEmail                    =models.BooleanField(default=False)
    status                       =models.BooleanField(default=False) 
    def __str__(self):
        return self.first_last_name
    
#######################################################################################



#######################################################################################