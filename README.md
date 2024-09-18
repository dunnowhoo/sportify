# Sportify
### Let Sportify be your rhythm to fitness success!
At Sportify, we believe that finding the right equipment, apparel, and supplements should be as easy as pressing play on your favorite workout playlist. Whether you're gearing up for the gym, a weekend hike, or training for your next competition, we've got everything you need to perform at your best.

## Tautan Aplikasi
[https://fauzan-putra31-sportify.pbp.cs.ui.ac.id/](http://fauzan-putra31-sportify.pbp.cs.ui.ac.id/)

## 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memastikan bahwa informasi yang dibutuhkan oleh pengguna atau sistem lain dapat dikirimkan dengan tepat waktu, dalam format yang sesuai, dan melalui media yang tepat. Dalam sebuah platform, data bisa berasal dari berbagai sumber dan dapat digunakan untuk berbagai keperluan, seperti memuat produk di halaman e-commerce, memproses transaksi, atau menampilkan konten dinamis. Tanpa mekanisme data delivery yang baik, platform mungkin tidak bisa berfungsi secara optimal karena data tidak sampai ke tujuan atau tidak tersedia sesuai kebutuhan pengguna.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON umumnya lebih baik daripada XML dalam konteks pengembangan web modern. JSON lebih ringan dan lebih mudah dibaca oleh manusia serta mesin. JSON juga lebih terintegrasi dengan JavaScript, yang menjadi bahasa utama dalam pengembangan aplikasi web. Ini membuat proses parsing dan manipulasi data jauh lebih efisien. Di sisi lain, XML memiliki fitur yang lebih kompleks seperti dukungan untuk skema dan namespace, namun biasanya fitur tersebut tidak terlalu diperlukan dalam aplikasi web yang sebagian besar hanya membutuhkan pertukaran data sederhana. Karena alasan-alasan tersebut, JSON menjadi lebih populer dibandingkan XML.

## 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan oleh pengguna ke dalam form memenuhi semua aturan validasi yang telah ditentukan. Method ini akan mengembalikan nilai True jika semua data valid, dan False jika ada data yang tidak valid. Kita membutuhkan method ini karena data yang dimasukkan oleh pengguna tidak selalu sesuai dengan format atau aturan yang diharapkan. Dengan memvalidasi data melalui `is_valid()`, kita dapat memastikan bahwa data yang diproses oleh aplikasi adalah data yang benar dan mencegah kesalahan yang dapat menyebabkan masalah saat data disimpan atau diproses.

## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` diperlukan pada form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang dapat menipu pengguna yang sudah diautentikasi untuk melakukan tindakan tidak diinginkan pada aplikasi web. Jika kita tidak menambahkan `csrf_token`, aplikasi tidak akan memiliki cara untuk memverifikasi apakah permintaan yang dikirim oleh pengguna memang berasal dari sumber yang sah atau hasil dari serangan. Penyerang dapat memanfaatkan kelemahan ini untuk mengirimkan permintaan berbahaya atas nama pengguna, misalnya melakukan perubahan data atau melakukan transaksi tanpa izin pengguna.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### **1. Implementasi Skeleton Sebagai Kerangka Views**

#### **Langkah 1: Membuat Template `base.html`**
- **Tujuan**: `base.html` akan berfungsi sebagai kerangka umum untuk seluruh halaman web.
- **Implementasi**: 
   - Buat direktori `templates` di root folder proyek.
   - Buat berkas `base.html` di dalam direktori `templates` yang akan menjadi kerangka dasar.
   - Dalam berkas ini, tambahkan blok `{% block content %}{% endblock %}` untuk bagian dinamis.

#### **Langkah 2: Mengkonfigurasi `settings.py`**
- **Tujuan**: Supaya template `base.html` dapat dikenali oleh Django.
- **Implementasi**:
   - Buka `settings.py`, cari bagian `TEMPLATES`.
   - Tambahkan direktori `templates` agar terdeteksi sebagai tempat penyimpanan berkas HTML.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        ...
    },
]
```

---

### **2. Mengubah Primary Key dari Integer Menjadi UUID**

#### **Langkah 3: Mengubah Model**
- **Tujuan**: Mengganti primary key `id` dari integer menjadi UUID.
- **Implementasi**: 
   - Buka `models.py` di dalam direktori `main/`.
   - Buat atau ubah model `Product` agar menggunakan UUID.

```python
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
```

#### **Langkah 4: Migrasi Model**
- **Tujuan**: Menerapkan perubahan model pada database.
- **Implementasi**:
   - Jalankan perintah berikut di terminal.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **3. Membuat Form Input dan Menampilkan Data `Product`**

#### **Langkah 5: Membuat Form di `forms.py`**
- **Tujuan**: Membuat form untuk menambahkan data `Product`.
- **Implementasi**:
   - Buat berkas `forms.py` di dalam direktori `main/`.
   - Tambahkan kode untuk form `ProductEntryForm`.

```python
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock"]
```

#### **Langkah 6: Menambahkan Fungsi di `views.py`**
- **Tujuan**: Membuat tampilan untuk form dan daftar produk.
- **Implementasi**:
   - Buka `views.py` di direktori `main/` dan import form serta model.
   - Tambahkan fungsi `create_product_entry` untuk menambahkan produk, dan `show_main` untuk menampilkan daftar produk.

```python
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product

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
```

#### **Langkah 7: Menambahkan URL pada `urls.py`**
- **Tujuan**: Agar URL bisa diakses di browser.
- **Implementasi**:
   - Buka `urls.py` dan tambahkan URL untuk fungsi `create_product_entry` dan `show_main`.

```python
from django.urls import path
from main.views import create_product_entry, show_main

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product-entry', create_product_entry name='create_product_entry'),
]
```

#### **Langkah 8: Membuat Template HTML**
- **Tujuan**: Menampilkan form dan daftar produk.
- **Implementasi**: 
   - Buat `create_product_entry.html` untuk form dan `product_list.html` untuk menampilkan daftar produk.

---

### **4. Menampilkan Data dalam Format XML dan JSON**

#### **Langkah 9: Membuat Views untuk XML dan JSON**
- **Tujuan**: Menampilkan data dalam format XML dan JSON.
- **Implementasi**: 
   - Buka `views.py` dan tambahkan fungsi `show_xml` dan `show_json`.

```python
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### **Langkah 10: Menambahkan URL untuk XML dan JSON**
- **Implementasi**: Buka `urls.py` dan tambahkan URL untuk kedua format tersebut.

```python
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
```

#### **Langkah 11: Menampilkan Data Berdasarkan ID**
- **Implementasi**: Tambahkan fungsi untuk menampilkan data `Product` berdasarkan `id` dalam format XML dan JSON.

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Tambahkan URL di `urls.py`:

```python
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

--- 
## Menampilkan JSON dan XML dengan Postman
### Menampilkan XML
<img width="777" alt="image" src="https://github.com/user-attachments/assets/ce1a7faf-55f2-442b-bfab-60275db3247f">

### Menampilkan JSON
<img width="777" alt="image" src="https://github.com/user-attachments/assets/27c64980-1463-4302-a287-29853d657aae">

### Menampilkan XML dan JSON by id
<img width="777" alt="image" src="https://github.com/user-attachments/assets/0b5c6aab-c5d9-4c38-ae73-f35ec9d93c75">
<img width="777" alt="image" src="https://github.com/user-attachments/assets/854f85d7-0274-45fb-8d1a-c2b1840d7f52">



