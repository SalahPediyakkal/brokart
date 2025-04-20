from django.contrib import admin
from orders.models import Order, OrderedItem

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        "owner",           
        "order_status"
    ]
    search_fields = [
        "owner__name",     
        "owner__user__username",  
        "id"
    ]

admin.site.register(Order, OrderAdmin)