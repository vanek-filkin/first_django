from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your

def index(request):
    new_prod_list = Product.objects.order_by('-rel_date')
    context = {'new_prod_list': new_prod_list}
    return render(request, 'products/index.html', context)

def detail(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    return render(request, 'products/detail.html', {'product': product})

def add_new(request):
    if request.method=="POST":
        q = Product(*data)
    return render(request, 'products/new_product.html')

def delete(request,prod_id):
    Product.objects.filter(id=prod_id).delete()
    new_prod_list = Product.objects.order_by('-rel_date')
    context = {'new_prod_list': new_prod_list}
    return render(request, 'products/index.html', context)