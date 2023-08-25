from django.contrib import admin

from catalog.models import Image, CatalogItems

admin.site.register(Image)
# admin.site.register(SalesItem)
admin.site.register(CatalogItems)
