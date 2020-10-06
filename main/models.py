from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.mail import send_mail
# Create your models here.
#
#
#
STOCK_CHOICES = ( 
    ("1", "Da."), 
    ("2", "Ne."), 
   
) 

class Item(models.Model):
    ime                        =models.CharField(max_length=150)
    opis                       =models.CharField(max_length=200)
    cena                       =models.IntegerField()
    lager = models.CharField(max_length=100)

        

    def __str__(self):
        return self.ime


######################################################################################
class Offer(models.Model):
    item                         =models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity1                     =models.IntegerField(null=False)   
    second                       =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='second', null=True, blank=True)
    quantity2                     =models.IntegerField(null=True, blank=True)
    third                        =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='third', null=True, blank=True)
    quantity3                    =models.IntegerField(null=True, blank=True)
    fourth                       =models.ForeignKey(Item, on_delete=models.CASCADE, related_name='fourth', null=True, blank=True)
    quantity4                     =models.IntegerField(null=True, blank=True)
    first_last_name              =models.CharField(max_length=120)
     
    phone_number                 =models.IntegerField() 
    email_address                =models.EmailField(null=True)   
    address                      =models.CharField(max_length=120)
    datetime                     =models.DateTimeField(null=True)
    finalOffer                   =models.IntegerField(null=True)
    sendEmail                    =models.BooleanField(default=False)
    status                       =models.BooleanField(default=False) 
    def __str__(self):
        return self.first_last_name

        
    def save(self):
        if self.sendEmail == True:
            send_mail("Potpala drvo ćumur ponuda.", 
            "Ukupna cena za vaše artikle je" +  " " + str(self.finalOffer) + "Odgovorite na ovaj email, da potvrdite kupovinu.", 
           "potpaladrvocumur@gmail.com", 
           [self.email_address], fail_silently=False)
        super().save()

    
#######################################################################################
class Message(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True, max_length=254)
    message = models.CharField(max_length=256, null=False)
    response = models.CharField(max_length=256, null=True)
    sendEmail = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def save(self):
        if self.sendEmail == True:
            send_mail("Odgovor", 
            str(self.response), 
           "potpaladrvocumur@gmail.com", 
           [self.email], fail_silently=False)
        super().save()

#######################################################################################