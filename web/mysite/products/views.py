from django.shortcuts import render,get_object_or_404
from .models import Product
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView,DetailView

# Create your
class ProductList(ListView):
    model = Product
    template_name = "products/index.html"
    def order_by_date(seld):
        return Product.objects.order_by('-rel_date')

# def index(request):
#     new_prod_list = Product.objects.order_by('-rel_date')
#     context = {'new_prod_list': new_prod_list}
#     return render(request, 'products/index.html', context)
class Show_detail(DetailView):
    model = Product
    template_name = "products/detail.html"
    context_object_name = "product"
    pk_url_kwarg = 'prod_id'
# def detail(request, prod_id):
#     product = get_object_or_404(Product, pk=prod_id)
#     return render(request, 'products/detail.html', {'product': product})

def add_new(request):
    if request.method == "POST":
        if request.FILES:
            file = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
        data = request.POST
        new_data = Product(name = data['name'],
                           type_of = data['category'],
                           manufacturer = data['manufacturer'],
                           country = data['country'],
                           description = data['description'],
                           price = int(data['price']),
                           rel_date = data['rel_date'],
                           img = request.FILES['photo']
                            )
        new_data.save()
        return HttpResponseRedirect('..')
    return render(request,'products/new_product.html')

def delete(request,prod_id):
    Product.objects.filter(id=prod_id).delete()
    return HttpResponseRedirect('../..')