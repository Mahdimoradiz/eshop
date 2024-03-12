from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import get_object_or_404
from product.models import Product
from cart.order import Cart


class CartDetailView(View):
    def get(self, request):
        # Create instance of card class using request
        cart = Cart(request)
        # Calculate the number of items in the card using Kant
        item_count = cart.count_items()
        context = {
            'cart': cart,
            'item_count': item_count
            }
        return render(request, "cart/cart_detail.html", context)
    
    
class CartAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        # Get product information from the request
        quantity =  request.POST.get('quantity')
        if quantity is not None:
            quantity = int(quantity)
        else:
            quantity = 1
        color = request.POST.get('color', 'empty')
        size = request.POST.get('size', 'empty')
        # Create instance of card class using request
        cart = Cart(request)
        # Add product to card
        cart.add(product, color, size, quantity)
        return redirect("cart:cart_detail")
   
  
class CartDeleteView(View):
    def get(self, request, id):
        # Create instance of card class using request
        cart = Cart(request)
        # Remove the product from the card 
        cart.delete(id)
        return redirect("cart:cart_detail")
    
    