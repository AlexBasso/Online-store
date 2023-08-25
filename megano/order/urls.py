from django.urls import path

from order.views import OrdersView, OrderView, PaymentView

urlpatterns = [
    path("orders", OrdersView.as_view(), name="orders"),
    path("order/<int:id>", OrderView.as_view(), name="order"),
    path("payment/<int:id>", PaymentView.as_view(), name="payment"),
]
