from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from product.models import Product
from cart.order import Cart


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart/cart_detail.html", {'cart': cart})
    
    
    
class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        print(size, color, quantity)
        cart = Cart(request)
        cart.add(product, quantity, color, size)
        return redirect("cart:cart_detail")
        