from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    
    product_entries = Product.objects.all()

    context = {
        'products': product_entries,
        'name': 'Fauzan Putra Sanjaya',
        'npm': '2306275424',
        'class': 'PBP A',
    }

    return render(request, "product_list.html", context)


def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    # Define some sample products
  #  products = [
  #      Product(name="Nike Air Jordan", price=200,
  #              description="The iconic Air Jordan with premium leather and superior comfort.", stock=5, image="products/nike.jpg"),
   #     Product(name="Adidas Yeezy Boost", price=300,
   #             description="Exclusive Yeezy Boost series with responsive cushioning and modern design.", stock=3, image="products/adidas.jpg"),
   #     Product(name="Puma RS-X", price=120,
   #             description="Retro-style Puma RS-X sneakers with bold color blocking.", stock=8, image="products/puma.jpg"),
   #     Product(name="New Balance 990v5", price=180,
   #             description="Classic New Balance 990v5 with superior stability.", stock=10, image="products/nb.jpg"),
   #     Product(name="Converse Chuck Taylor All Star", price=60,
    #            description="Timeless Chuck Taylor All Star sneakers with canvas upper.", stock=15, image="products/converse.jpg"),
    #    Product(name="Reebok Classic Leather", price=90,
   #             description="Classic Reebok design with leather upper and EVA midsole.", stock=12, image="products/rebook.jpg"),
   #     Product(name="Vans Old Skool", price=70,
   #             description="Classic skate shoes with durable suede and cool canvas construction.", stock=20, image="products/vans.jpg"),
   #     Product(name="Under Armour HOVR Phantom", price=140,
   #             description="High-performance running shoes with UA HOVR cushioning.", stock=7, image="products/UA.jpg"),
 #   ]

