from django.contrib import admin

from order.models import Order, OrderedProduct, OrderImage

admin.site.register(Order)
admin.site.register(OrderedProduct)
admin.site.register(OrderImage)
