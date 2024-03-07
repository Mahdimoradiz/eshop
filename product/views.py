from django.shortcuts import render, HttpResponse
from django.views.generic import DeleteView

from product.models import Product


class ProductDetail(DeleteView):
    model = Product
    template_name = "product/product.html"
    