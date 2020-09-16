from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
#
#
#

class Item(models.Model):
    name                         =models.CharField(max_length=150)
    description                  =models.CharField(max_length=200)
    price                        =models.IntegerField()

    def __str__(self):
        return self.name


######################################################################################
class Offer(models.Model):
    item                         =models.ForeignKey(Item, on_delete=models.CASCADE)
    first_last_name              =models.CharField(max_length=120)
    quantity                     =models.IntegerField()   
    phone_number                 =models.IntegerField() 
    email_address                =models.EmailField(null=False)   
    address                      =models.CharField(max_length=120)
    datetime                     =models.DateTimeField()
    finalOffer                   =models.IntegerField()
    sendEmail                    =models.BooleanField(default=False)

    def __str__(self):
        return self.first_last_name
    
#######################################################################################



#######################################################################################