# Sportify
### Let Sportify be your rhythm to fitness success!
At Sportify, we believe that finding the right equipment, apparel, and supplements should be as easy as pressing play on your favorite workout playlist. Whether you're gearing up for the gym, a weekend hike, or training for your next competition, we've got everything you need to perform at your best.

## Tautan Aplikasi
[https://fauzan-putra31-sportify.pbp.cs.ui.ac.id/](http://fauzan-putra31-sportify.pbp.cs.ui.ac.id/)


# Tugas 5 
## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Ketika beberapa CSS selector diterapkan pada elemen yang sama, urutan prioritas (specificity) menentukan aturan mana yang diambil. Prioritas ditentukan oleh "specificity" dari selector tersebut, diurutkan dari yang paling rendah ke yang paling tinggi sebagai berikut:
- Tag Selector (misalnya div, p, h1) memiliki prioritas terendah.
- Class Selector (misalnya .class-name) memiliki prioritas lebih tinggi dari tag selector.
- ID Selector (misalnya #id-name) memiliki prioritas lebih tinggi dari class selector.
- Inline Styles (CSS yang langsung diletakkan pada elemen menggunakan atribut style="") memiliki prioritas tertinggi.
- !important: Properti dengan deklarasi !important akan mengesampingkan aturan lainnya, kecuali jika ada aturan lain dengan !important dan specificity yang lebih tinggi.

Contoh:
```css
div { color: blue; }  /* Tag selector */
.class-name { color: red; }  /* Class selector */
#id-name { color: green; }  /* ID selector */
<div id="id-name" class="class-name">Text</div>
```
Pada elemen tersebut, warna yang diambil adalah hijau karena ID selector memiliki prioritas tertinggi.
## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah konsep yang memastikan bahwa tampilan website atau aplikasi web dapat beradaptasi dengan berbagai ukuran layar dan perangkat (misalnya desktop, tablet, smartphone). Hal ini penting karena:

- Pengalaman Pengguna (User Experience): Pengguna yang menggunakan perangkat dengan ukuran layar berbeda dapat tetap mengakses konten dengan nyaman tanpa harus memperbesar/memperkecil tampilan.
- SEO: Google mengutamakan website yang mobile-friendly dalam hasil pencarian, sehingga responsive design dapat meningkatkan ranking SEO.
- Aksesibilitas: Membuat aplikasi lebih mudah diakses oleh semua orang, termasuk mereka yang menggunakan perangkat mobile atau tablet.

Contoh Aplikasi:

- Sudah Menerapkan Responsive Design: Twitter dan Facebook, yang layout dan kontennya menyesuaikan ukuran layar perangkat pengguna.
- Belum Menerapkan Responsive Design: Situs yang lebih lama dan tidak teroptimasi, seperti beberapa portal berita lama yang tidak menyesuaikan layout pada perangkat mobile.
## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: Ruang di luar border yang mengatur jarak antara elemen dengan elemen lain di luar elemen tersebut.
- Border: Garis yang membungkus elemen, di antara padding dan margin.
- Padding: Ruang di dalam border, mengatur jarak antara konten elemen dan border elemen.

Contoh Implementasi:

```css
div {
  margin: 20px;  /* Ruang di luar border */
  border: 1px solid black;  /* Garis di sekitar elemen */
  padding: 10px;  /* Ruang antara border dan konten */
}
```
Margin akan memberikan ruang di luar elemen div.
Border membungkus elemen div.
Padding akan membuat jarak antara konten dan border elemen div.
## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox: Flexbox (Flexible Box Layout) adalah metode tata letak satu dimensi (horizontal atau vertikal) yang mempermudah pengaturan layout item dalam sebuah container. Flexbox sangat cocok untuk mengatur elemen dalam satu baris atau kolom yang fleksibel dan responsif.

Kegunaan: Flexbox sering digunakan untuk membuat elemen-elemen dalam container dapat diratakan (aligned), didistribusikan (distributed), dan diatur (ordered) dengan mudah.

Contoh:

```css
.container {
  display: flex;
  justify-content: space-between;  /* Atur jarak antar item */
  align-items: center;  /* Atur posisi vertikal item */
}
```
Flexbox sangat berguna untuk hal-hal seperti navigasi horizontal, tombol, dan elemen layout responsif yang fleksibel.

- Grid Layout: Grid Layout adalah metode tata letak dua dimensi (baris dan kolom) yang memungkinkan pembagian ruang halaman web secara lebih kompleks dan terstruktur. Ini memungkinkan pengembang untuk membuat grid yang terdiri dari kolom dan baris, dan mengatur elemen-elemen dalam grid dengan sangat presisi.

Kegunaan: Grid layout cocok untuk layout yang lebih kompleks seperti dashboard atau halaman yang memiliki banyak elemen dengan ukuran dan posisi yang beragam.

Contoh:
```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;  /* 3 kolom dengan proporsi berbeda */
  grid-template-rows: auto;
  gap: 10px;  /* Jarak antar kolom dan baris */
}
```
Flexbox untuk satu dimensi, sedangkan Grid Layout lebih cocok untuk pengaturan tata letak dua dimensi.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
## Mengimplementasikan Fitur Edit dan Hapus Produk

### 1. **Buat Fungsi Edit Produk di `views.py`:**
   - Buka file `views.py` di subdirektori `main`.
   - Tambahkan fungsi `edit_product` untuk menangani proses pengeditan produk:
     ```python
     from django.shortcuts import get_object_or_404, render, redirect
     from .models import Product
     from .forms import ProductEntryForm

     def edit_product(request, id):
         # Ambil produk berdasarkan id dengan get_object_or_404
         product = get_object_or_404(Product, pk=id)

         # Inisialisasi form dengan instance produk
         form = ProductEntryForm(request.POST or None, request.FILES or None, instance=product)

         if request.method == "POST" and form.is_valid():
             # Simpan form dan kembali ke halaman utama
             form.save()
             return redirect('main:show_main')

         # Jika request bukan POST atau form tidak valid, render template
         context = {'form': form}
         return render(request, 'edit_product.html', context)
     ```

### 2. **Buat Fungsi Hapus Produk di `views.py`:**
   - Masih di file yang sama, tambahkan fungsi `delete_product` untuk menangani penghapusan produk:
     ```python
     def delete_product(request, id):
         # Ambil produk berdasarkan id dengan get_object_or_404
         product = get_object_or_404(Product, pk=id)

         # Hapus produk
         product.delete()

         # Kembali ke halaman utama setelah delete
         return redirect('main:show_main')
     ```

### 3. **Update URL Patterns di `urls.py`:**
   - Buka file `urls.py` di subdirektori `main`.
   - Tambahkan path untuk edit dan delete produk:
     ```python
     from django.urls import path
     from .views import edit_product, delete_product

     urlpatterns = [
         path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
         path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
     ]
     ```

### 4. **Buat Template `edit_product.html`:**
   - Buat file baru bernama `edit_product.html` di direktori template.
   - Gunakan kode berikut untuk form edit produk:
     ```html
     {% extends 'base.html' %}
     {% load static %}
     {% block meta %}
     <title>Edit Product</title>
     <style>
         .form-input {
             width: calc(100% - 20px); /* Adjust to include padding */
             background-color: black; /* Set background color to black */
             border: none; /* Remove default border */
             border-radius: 5px; /* Add rounded corners */
             color: black; /* Set text color to white */
             padding: 10px; /* Add padding for better spacing */
             box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Optional: add a subtle shadow */
             outline: none; /* Remove outline */
         }
         .form-input:focus {
             border: 2px solid #1db954; /* Change border color on focus */
             background-color: #111; /* Darker background on focus */
         }
     </style>
     {% endblock meta %}

     {% block content %}
     {% include 'navbar.html' %}

     <div class="flex flex-col min-h-screen bg-black">
         <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
             <h1 class="text-3xl font-bold text-center mb-8 text-white">Edit Product Entry</h1>

             <div class="bg-gray-800 rounded-lg p-6">
                 <form method="POST" class="space-y-6">
                     {% csrf_token %}
                     {% for field in form %}
                     <div class="flex flex-col">
                         <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-300">
                             {{ field.label }}
                         </label>
                         <div class="w-full">
                             {{ field }}
                         </div>
                         {% if field.help_text %}
                         <p class="mt-1 text-sm text-black">{{ field.help_text }}</p>
                         {% endif %}
                         {% for error in field.errors %}
                         <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                         {% endfor %}
                     </div>
                     {% endfor %}
                     <div class="flex justify-center mt-6">
                         <button type="submit"
                             class="bg-green-500 text-white font-semibold px-6 py-3 rounded-lg hover:bg-green-500 transition duration-300 ease-in-out w-full">
                             Save Changes
                         </button>
                     </div>
                 </form>
             </div>
         </div>
     </div>
     {% endblock %}
     ```

### 5. **Update Template `product_list.html`:**
   - Tambahkan tombol edit dan delete di setiap item produk:
     ```html
     <div class="product-actions mt-4">
         <a href="{% url 'main:edit_product' product.id %}"
             class="edit-button bg-yellow-500 hover:bg-yellow-600 text-white rounded p-2 transition duration-300 shadow-md flex items-center">
             <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                 <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
             </svg>
         </a>
         <form action="{% url 'main:delete_product' product.id %}" method="POST" class="delete-form"
             onsubmit="return confirm('Are you sure you want to delete this product?');" style="display:inline;">
             {% csrf_token %}
             <button type="submit"
                 class="delete-button bg-red-500 hover:bg-red-600 text-white rounded p-2 transition duration-300 shadow-md flex items-center">
                 <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                     <path fill-rule="evenodd"
                         d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                         clip-rule="evenodd"/>
                 </svg>
             </button>
         </form>
     </div>
     ```

### 6. **Kustomisasi Login, Register, Homepage:**
   -  Kustomisasi Login, Register, Homepage sudah dilkaukan di tugas sebelumnya.

### 7. **Cek Kembali Semua Fitur:**
   - Setelah implementasi selesai, pastikan untuk menguji semua fitur (edit dan hapus produk) di aplikasi untuk memastikan semuanya berjalan dengan baik dan tanpa error.


# Tugas 4
## 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
`HttpResponseRedirect()` : adalah kelas dari Django yang digunakan untuk mengalihkan permintaan ke URL tertentu. Kita harus mengimpor HttpResponseRedirect dari django.http dan memberikan URL yang ingin dituju.
```python
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
```
`redirect()` : adalah fungsi yang lebih umum dan lebih mudah digunakan. redirect() dapat menerima URL, nama view, atau objek model, dan secara otomatis menghasilkan objek `HttpResponseRedirect`.
```python
from django.shortcuts import redirect

def my_view(request):
    return redirect('/some-url/')
```
`redirect()` juga menangani resolusi URL dengan lebih baik dan dapat digunakan dengan nama view, misalnya redirect('view_name')

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model Product dengan model User bisa menggunakan ForeignKey. Ini memungkinkan setiap produk terhubung dengan pengguna yang meng-upload produk tersebut.

Contoh model Product yang dihubungkan dengan User:
```python
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
```
Dalam contoh di atas, ForeignKey digunakan untuk membuat hubungan satu-ke-banyak antara User dan Product. Setiap produk akan terkait dengan satu pengguna, dan jika pengguna dihapus, semua produk yang terkait juga akan dihapus (karena on_delete=models.CASCADE).

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
#### Authentication (Otentikasi):
Proses verifikasi identitas pengguna. Misalnya, saat pengguna memasukkan username dan password, sistem memeriksa apakah kredensial tersebut benar.
Pada saat pengguna login, proses ini yang dilakukan untuk memastikan bahwa pengguna yang masuk adalah orang yang mereka klaim.
#### Authorization (Otorisasi):
Proses untuk menentukan hak akses pengguna setelah mereka terotentikasi. Ini menentukan apa yang pengguna dapat dan tidak dapat lakukan di dalam aplikasi.
#### Implementasi di Django:
Django menyediakan sistem otentikasi built-in yang mengelola otentikasi dan otorisasi. Saat pengguna login, Django memeriksa kredensialnya dan membuat sesi untuk pengguna tersebut jika otentikasi berhasil. Kita dapat menggunakan decorators seperti @login_required untuk membatasi akses ke view tertentu hanya untuk pengguna yang terotentikasi.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan sesi untuk menyimpan informasi pengguna yang terotentikasi. Ketika pengguna login, Django membuat sesi dan menyimpan ID pengguna di dalamnya. Informasi sesi ini disimpan dalam cookies di sisi klien, sehingga setiap kali pengguna mengunjungi halaman lain, Django dapat mengambil ID pengguna dari cookie dan mengidentifikasi sesi pengguna.

#### Kegunaan Lain dari Cookies:

Menyimpan preferensi pengguna, seperti bahasa atau tema yang dipilih.
Mengingat isi keranjang belanja dalam aplikasi e-commerce.
Menganalisis perilaku pengguna di situs web untuk meningkatkan pengalaman pengguna.

#### Apakah Semua Cookies Aman Digunakan?:
Tidak semua cookies aman. Cookies dapat digunakan untuk menyimpan data sensitif, dan jika tidak dikelola dengan baik, dapat menjadi celah keamanan.

#### Jenis cookies:
- Session Cookies: Hanya berlaku selama sesi pengguna dan dihapus saat browser ditutup.
- Persistent Cookies: Dapat tetap ada di perangkat pengguna untuk jangka waktu tertentu.
- HttpOnly Cookies: Tidak dapat diakses melalui JavaScript, membantu melindungi dari serangan XSS.
- Secure Cookies: Hanya dikirim melalui koneksi HTTPS, membantu melindungi data selama transmisi.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Mengimplementasikan Fungsi Registrasi, Login, dan Logout

1. **Aktifkan Virtual Environment:**
   - Pastikan virtual environment Anda sudah aktif. Jika belum, jalankan perintah di terminal:
     ```bash
     source env/bin/activate
     ```

2. **Buka `views.py` di Subdirektori `main`:**
   - Tambahkan `UserCreationForm` dan `messages` di bagian paling atas file `views.py`:
     ```python
     from django.contrib.auth.forms import UserCreationForm
     from django.contrib import messages
     ```



3. **Tambahkan Fungsi Registrasi:**
   - Tambahkan kode berikut di dalam file `views.py` untuk menangani registrasi pengguna:
     ```python
     def register(request):
         form = UserCreationForm()

         if request.method == "POST":
             form = UserCreationForm(request.POST)
             if form.is_valid():
                 form.save()
                 messages.success(request, 'Your account has been successfully created!')
                 return redirect('main:login')

         context = {'form': form}
         return render(request, 'register.html', context)
     ```

4. **Buat Template `register.html`:**
   - Buat file HTML baru bernama `register.html` di direktori `main/templates` dengan isi berikut:
     ```html
        {% block content %}
        <div class="auth-container">
            <div class="auth-form">
                <div class="auth-logo-container">
                    <img src="https://i.imgur.com/wKHhTQw.png" alt="Logo" class="auth-logo">
                    <span class="auth-logo-text">Sportify</span>
                </div>
                <div class="auth-tabs">
                    <a href="{% url 'main:login' %}" class="auth-tab">SIGN IN</a>
                    <span class="auth-tab active">SIGN UP</span>
                </div>

                <form method="POST">
                    {% csrf_token %}
                    <div class="auth-input">
                        <input type="text" name="username" placeholder="Username" required />
                    </div>
                    <div class="auth-input">
                        <input type="email" name="email" placeholder="Email" required />
                    </div>
                    <div class="auth-input">
                        <input type="password" name="password1" placeholder="Password" required />
                    </div>
                    <div class="auth-input">
                        <input type="password" name="password2" placeholder="Confirm Password" required />
                    </div>
                    <div class="auth-submit">
                        <button type="submit" class="btn auth-btn">Sign Up</button>
                    </div>
                </form>
            </div>
        </div>
        {% endblock content %}
     ```

5. **Tambahkan Route untuk Registrasi di `urls.py`:**
   - Buka `urls.py` di subdirektori `main` dan tambahkan import serta path untuk fungsi `register`:
     ```python
     from main.views import register

     urlpatterns = [
         # ... URL lainnya
         path('register/', register, name='register'),
     ]
     ```

6. **Fungsi Login:**
   - Tambahkan import `authenticate`, `login`, dan `AuthenticationForm` di `views.py`:
     ```python
     from django.contrib.auth.forms import AuthenticationForm
     from django.contrib.auth import authenticate, login
     ```

   - Implementasikan fungsi login:
     ```python
     def login_user(request):
         if request.method == 'POST':
             form = AuthenticationForm(data=request.POST)

             if form.is_valid():
                 user = form.get_user()
                 login(request, user)
                 return redirect('main:show_main')

         else:
             form = AuthenticationForm()

         context = {'form': form}
         return render(request, 'login.html', context)
     ```

7. **Buat Template `login.html`:**
   - Buat file `login.html` di direktori `main/templates`:
     ```html
        {% block content %}
        <div class="auth-container">
            <div class="auth-form">
                <div class="auth-logo-container">
                    <img src="https://i.imgur.com/wKHhTQw.png" alt="Logo" class="auth-logo">
                    <span class="auth-logo-text">Sportify</span>
                </div>
                <div class="auth-tabs">
                    <span class="auth-tab active">SIGN IN</span>
                    <a href="{% url 'main:register' %}" class="auth-tab">SIGN UP</a>
                </div>

                <form method="POST">
                    {% csrf_token %}
                    <div class="auth-input">
                        <input type="text" name="username" placeholder="Username" required />
                    </div>
                    <div class="auth-input">
                        <input type="password" name="password" placeholder="Password" required />
                    </div>
                    <div class="auth-checkbox">
                        <input type="checkbox" id="stay_signed_in">
                        <label for="stay_signed_in">Stay signed in</label>
                    </div>
                    <div class="auth-submit">
                        <button type="submit" class="btn auth-btn">Sign In</button>
                    </div>
                </form>

                <a href="#" class="forgot-password">Forgot Password?</a>
            </div>
        </div>
        {% endblock content %}
     ```

8. **Tambahkan Route untuk Login di `urls.py`:**
   - Buka `urls.py` di subdirektori `main` dan tambahkan route untuk fungsi `login_user`:
     ```python
     from main.views import login_user

     urlpatterns = [
         # ... URL lainnya
         path('login/', login_user, name='login'),
     ]
     ```

9. **Fungsi Logout:**
   - Tambahkan import `logout` di `views.py`:
     ```python
     from django.contrib.auth import logout
     ```

   - Implementasikan fungsi logout:
     ```python
     def logout_user(request):
         logout(request)
         return redirect('main:login')
     ```

10. **Tambahkan Tombol Logout di Template:**
    - Di file `main.html`, tambahkan tombol logout di dalam template:
      ```html
      <a href="{% url 'main:logout' %}">
        <button>Logout</button>
      </a>
      ```

11. **Tambahkan Route untuk Logout di `urls.py`:**
    - Buka `urls.py` dan tambahkan path untuk fungsi `logout_user`:
      ```python
      from main.views import logout_user

      urlpatterns = [
          # ... URL lainnya
          path('logout/', logout_user, name='logout'),
      ]
      ```
### Membuat Dua Akun Pengguna dengan  Tiga Dummy Data
#### 1. **Buat Akun Baru (Sign Up)**
   Klik tombol **Sign Up**, kemudian masukkan informasi yang diperlukan seperti:
   - **Username**
   - **Email**
   - **Password**
   - **Confirm Password**

   Setelah itu, klik tombol **Register** untuk membuat akun baru.
   
   ![Sign Up](https://i.imgur.com/FlaezLJ.png)

#### 2. **Login ke Akun (Sign In)**
   Masuk dengan menggunakan **username** dan **password** yang telah didaftarkan pada langkah sebelumnya. Isi form login dan klik tombol **Login** untuk mengakses aplikasi.

   ![Sign In](https://i.imgur.com/Jig66Qz.png)

#### 3. **Lihat Profil**
   Setelah berhasil login, klik tombol **Profile** di bagian atas atau kanan halaman. Di halaman ini, Anda akan melihat informasi pengguna yang sedang login, seperti **username** yang sesuai dengan akun yang baru saja Anda buat.

   ![User Profile](https://i.imgur.com/rrrhK22.png)

#### 4. **Tambah Produk Baru**
   Klik tombol **+** untuk menambahkan produk. Isi informasi produk seperti:
   - **Product Name**
   - **Price**
   - **Description**
   - **Stock**
   - Upload gambar produk.

   Setelah semua informasi diisi, klik tombol **Submit** untuk menyimpan produk.

   ![Add Product](https://i.imgur.com/Ezjn3rW.png)

#### 5. **Lihat Produk di Recent Product**
   Produk yang telah ditambahkan akan muncul di bagian **Recent Products** pada halaman utama. Produk akan tampil dengan informasi seperti nama produk, harga, deskripsi singkat, dan gambar produk.

   ![Recent Products](https://i.imgur.com/8cGsHd5.png)

#### 6. **Tambahkan 3 Produk Dummy**
   Ulangi proses menambahkan produk hingga ada tiga produk dummy pada akun pertama. Misalnya, produk-produk berikut:
   - **Produk 1:** "Adidas Yeezy" ($ 1.000)
   - **Produk 2:** "Nike Air Jordan" ($ 500)
   - **Produk 3:** "Converse" ($600)

#### 7. **Ulangi untuk Akun Lain**
   Logout dari akun pertama, kemudian login dengan akun pengguna lainnya. Ulangi langkah-langkah di atas untuk menambahkan tiga produk dummy lagi pada akun tersebut.

   ![User 2 Products](https://i.imgur.com/DExbXOq.png)

Dengan cara ini, setiap akun akan memiliki tiga produk dummy yang muncul di halaman **Recent Products**.

### Menghubungkan Model Product dengan User
#### 1. **Modifikasi models.py**
   Buka file `models.py` di dalam subdirektori **main** dan tambahkan import untuk model **User**:

   ```python
   from django.contrib.auth.models import User
   ```

   Kemudian, tambahkan relasi **ForeignKey** ke dalam model **Product**:

   ```python
   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       # atribut produk lainnya
   ```

   **Penjelasan Kode**:
   - `user = models.ForeignKey(User, on_delete=models.CASCADE)` menghubungkan satu produk dengan satu pengguna melalui **ForeignKey**. Relasi ini memastikan bahwa setiap produk hanya dapat dimiliki oleh satu pengguna.
   - `on_delete=models.CASCADE` memastikan bahwa jika pengguna dihapus, semua produk yang terkait dengannya juga akan dihapus.

#### 2. **Modifikasi views.py**
   Buka file `views.py` di dalam subdirektori **main**. Pada fungsi untuk menambahkan produk, modifikasi kode seperti ini:

   ```python
   def add_product(request):
       form = ProductForm(request.POST or None, request.FILES or None)

       if form.is_valid() and request.method == "POST":
           product = form.save(commit=False)
           product.user = request.user
           product.save()
           return redirect('main:show_main')

       context = {'form': form}
       return render(request, "add_product.html", context)
   ```

   **Penjelasan Kode**:
   - `product.user = request.user`: Mengisi field **user** pada produk dengan pengguna yang sedang login.
   - `commit=False`: Mencegah Django menyimpan objek produk langsung ke database, sehingga kita bisa menambahkan data **user** terlebih dahulu sebelum menyimpannya.

#### 3. **Modifikasi Tampilan Produk (views.py)**
   Untuk memastikan hanya produk yang dimiliki oleh pengguna yang sedang login muncul di halaman utama, modifikasi fungsi yang menampilkan produk seperti ini:

   ```python
   def show_main(request):
       products = Product.objects.filter(user=request.user)

       context = {
           'products': products,
           'username': request.user.username,
       }
       return render(request, 'main.html', context)
   ```

   **Penjelasan Kode**:
   - `Product.objects.filter(user=request.user)`: Mengambil semua produk yang dibuat oleh pengguna yang sedang login.
   - `request.user.username`: Menampilkan **username** pengguna yang sedang login di halaman utama.

#### 4. **Migrasi Model**
   Setelah semua perubahan di `models.py` dilakukan, jalankan perintah berikut untuk membuat dan menerapkan migrasi:

   ```bash
   python manage.py makemigrations
   ```

   Saat menjalankan perintah ini, jika ada data produk di database tanpa user yang terkait, Anda akan diminta untuk memilih default value untuk field **user**. Pilih opsi yang sesuai untuk menyelesaikan migrasi. Setelah itu, jalankan:

   ```bash
   python manage.py migrate
   ```

#### 5. **Coba Aplikasi**
   Jalankan aplikasi Django dengan perintah:

   ```bash
   python manage.py runserver
   ```
   Sekarang, setiap produk yang dibuat akan terkait dengan pengguna yang menambahkannya, dan hanya bisa dilihat oleh pengguna tersebut.
### Menampilkan Detail Informasi Pengguna yang Sedang Logged In
#### 1. **Modifikasi views.py**

Pada file `views.py`, sesuaikan fungsi yang menampilkan halaman utama (atau halaman lain di mana Anda ingin menampilkan informasi pengguna yang login) seperti berikut:

```python
@login_required(login_url='/login')
def show_main(request):
    # Query all product entries
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'npm': '2306275424',
        'class': 'PBP A',
        'products': product_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "product_list.html", context)
```

**Penjelasan Kode**:
- `request.user.username`: Mengambil **username** pengguna yang sedang login.
- `request.COOKIES.get('last_login')`: Mengambil informasi **last login** dari cookies.

#### 2. **Modifikasi Template HTML**

Pada template `main.html`, tambahkan kode untuk menampilkan informasi pengguna yang login, seperti username dan last login.

#### 3. **Penggunaan Cookies Last Login**

Untuk memastikan cookies **last_login** tersimpan dengan benar saat pengguna login, pastikan fungsi login di `views.py` diatur seperti ini:

```python
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

Dengan kode di atas, saat pengguna berhasil login, waktu **last login** akan tersimpan di cookies dan ditampilkan pada halaman utama.
# Tugas 3
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

# Tugas 2
## Implementasi Checklist

1. Membuat proyek Django baru dengan perintah 
```
django-admin startproject sportify
```
2. Aktifkan virtual environment
```
source env/bin/activate
```
3. Masuk ke direktori proyek sportify dan buat aplikasi baru dengan nama main
```
python manage.py startapp main
```
3. Mengatur routing di `sportify/urls.py` untuk mengarahkan ke aplikasi `main`.
4. Tambahkan aplikasi main ke INSTALLED_APPS di file settings.py dalam proyek Django.

5. Membuat model `Product` dengan atribut `name`, `image`, `price`, `stok`, dan `description`.
6. Jalankan migrasi untuk menerapkan perubahan ke database:
```
python manage.py makemigrations
python manage.py migrate
```
7. Membuat fungsi `show_main` di `views.py` untuk menampilkan nama aplikasi, nama,kelas, dan detail produk.
8. Mengatur routing di `main/urls.py`.
9. Buat folder templates di dalam direktori proyek dan tambahkan file HTML
6. Buat folder static di dalam direktori proyek dan tambahkan file CSS
6. Buat folder media di dalam direktori proyek dan tambahkan foto produk.
6. Hapus entri untuk media dari file .gitignore agar file media dapat di-push ke PWS.

8. Menjalankan `collectstatic` untuk mengumpulkan file static.
```
python manage.py collectstatic
```
14. Melakukan deployment ke PWS.

## Bagan Request-Response Django

![image](https://github.com/user-attachments/assets/7e5edb3d-7a94-42ee-8b77-878bb7471dcc)


Bagan ini menjelaskan proses request dari client ke server Django:
- **Client** mengirim request ke **urls.py**.
- **urls.py** memetakan request ke **views.py**.
- **views.py** mengambil data dari **models.py** jika diperlukan dan merender **template HTML**.
- **Template HTML** dikembalikan sebagai respons ke client.

## Fungsi Git dalam Pengembangan Perangkat Lunak
Git digunakan untuk mengelola versi perangkat lunak, memungkinkan kolaborasi tim, tracking perubahan kode, dan rollback ke versi sebelumnya jika diperlukan.Git sangat membantu dalam memfasilitasi kerja kelompok dalam pengembangan perangkat lunak, termasuk untuk proyek-proyek mata kuliah seperti Pemrograman Berbasis Platform (PBP)

## Mengapa Django Digunakan?
Django dipilih karena menyediakan pendekatan full-stack dengan konsep MVT (Model-View-Template), mendukung ORM, dan memiliki fitur bawaan yang lengkap seperti autentikasi, admin, dan migrasi database.

## Mengapa Django Menggunakan ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis kueri SQL secara manual. ORM meningkatkan produktivitas dan mengurangi kesalahan dalam mengelola data.




