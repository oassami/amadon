from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all(),
        "all_orders": Order.objects.all(),
    }
    return render(request, "store/index.html", context)

def checking_out(request, product_id):
    product=Product.objects.get(id=product_id)
    quantity_from_form = int(request.POST["quantity"])
    total_charge = quantity_from_form * product.price
    print("Charging credit card...")
    order=Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(f'/checkout/{order.id}')

def checkout(request, order_id):
    # last_order = Order.objects.get(id=order_id)
    context={}
    sums=Order.objects.aggregate(Sum('quantity_ordered'), Sum('total_price'))
    context['qty_so_far']= str(sums['quantity_ordered__sum'])
    context['total_so_far']= str(round(sums['total_price__sum'],2))
    context['last_order'] = str(Order.objects.get(id=order_id).total_price)
    return render(request, "store/checkout.html", context)
