from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product
from cart.models import OrderItem


class Home(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suggeste_header"] = Product.objects.first()
        context["product"] = Product.objects.all()
        context["item"] = OrderItem.objects.all().count()
        return context