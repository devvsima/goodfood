from django.shortcuts import render, redirect

from catalog.models import Goods
from .models import Cart

def cart_add(request, product_slug):
    product = Goods.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)



    return redirect(request.META["HTTP_REFERER"])

def cart_change(request, product_slug):
    context = {
        "title": 'Carts',
    }

    return render(request, "", context)

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart.id)
    cart.delete()
    return redirect(request.META["HTTP_REFERER"])

