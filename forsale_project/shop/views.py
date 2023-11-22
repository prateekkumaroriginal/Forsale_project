from django.shortcuts import render
from .models import Product, Order
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


def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items', '')
        firstname = request.POST.get('firstName', '')
        lastname = request.POST.get('lastName', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        country = request.POST.get('country', '')
        state = request.POST.get('state', '')
        zipcode = request.POST.get('zipcode', '')
        total = request.POST.get('total', '')
        print(total)
        Order.objects.create(total=total,items=items,firstname=firstname,lastname=lastname,email=email,address=address,country=country,state=state,zipcode=zipcode)
    
    return render(request, 'shop/checkout.html')