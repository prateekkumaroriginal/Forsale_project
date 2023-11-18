from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    product_objects = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name is not None and item_name != "":
        product_objects = product_objects.filter(title__icontains=item_name)
    
    # pagination
    paginator = Paginator(product_objects, 2)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {"product_objects":product_objects})

def detail(request, product_id):
    product_object = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product_object': product_object})



