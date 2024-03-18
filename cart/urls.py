from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('detail', views.CartDetailView.as_view(), name="cart_detail"),
    path('add/<int:pk>', views.CartAddView.as_view(), name="cart_add"),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name="delete_item_cart"),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name="order_detail"),
    path('order/add', views.OrderCreationView.as_view(), name="order_create"),
    path('discount/<int:pk>', views.ApplyDiscountCodeVeiw.as_view(), name="discount_view"),
]
