from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('<int:pk>', views.ProductDetail.as_view(), name="product_detail")
]
