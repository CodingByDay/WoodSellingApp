from django.contrib import admin
from .models import Offer, Item, Message
# Register your models here.
from django.contrib.auth.admin import UserAdmin

class OfferAdmin(UserAdmin):
    list_display = ('item', 'phone_number', 'address', 'finalOffer', 'status')
    search_fields = ["item", "phone_number", "address", "finalOffer", "status"]
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()

    fieldsets = ()   
    
    ordering = ('item', 'phone_number', 'address', 'finalOffer', 'status')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Item)
class MessageAdmin(UserAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ["name", "email", "message"]
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()

    fieldsets = ()   
    
    ordering = ('name', 'email', 'message')
admin.site.register(Message, MessageAdmin)
