from django.contrib import admin

from product.models import Product, Image

# admin.site.register(Product)
admin.site.register(Image)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "category", "get_tags"]
    list_display_links = ["title"]

    def get_tags(self, obj):
        if obj.tags.all():
            return list(obj.tags.all().values_list("name", flat=True))
        else:
            return "NA"
