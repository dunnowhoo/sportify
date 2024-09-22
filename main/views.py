from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers


def show_main(request):
    # Query all product entries
    product_entries = Product.objects.all()

    context = {
        'products': product_entries,
        'name': 'Fauzan Putra Sanjaya',
        'npm': '2306275424',
        'class': 'PBP A',
    }

    return render(request, "product_list.html", context)


def create_product_entry(request):
    if request.method == 'POST':
        form = ProductEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Kembali ke halaman utama setelah berhasil menyimpan
            return redirect('main:show_main')

    else:
        form = ProductEntryForm()

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
