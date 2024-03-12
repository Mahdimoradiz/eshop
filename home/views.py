from django.shortcuts import render
from django.views.generic import TemplateView
from product.models import Product


class Home(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suggeste_header"] = Product.objects.filter(suggeste=True)
        context["product"] = Product.objects.all()
        return context


def person(request):
    pass