from django.urls import path

from catalog.views import (
    BannersView,
    CategoriesView,
    CatalogView,
    ProductsPopularView,
    ProductsLimitedView,
    SalesView,
)

urlpatterns = [
    path("banners", BannersView.as_view(), name="banners"),
    path("categories", CategoriesView.as_view(), name="categories"),
    path("catalog", CatalogView.as_view(), name="categories"),
    path("products/popular", ProductsPopularView.as_view(), name="products_popular"),
    path("products/limited", ProductsLimitedView.as_view(), name="products_limited"),
    path("sales", SalesView.as_view(), name="sales"),
]
