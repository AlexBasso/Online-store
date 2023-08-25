from django.contrib import admin

from basket.models import Basket, OrderProduct

admin.site.register(Basket)
admin.site.register(OrderProduct)
