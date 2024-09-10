# Sportify

Aplikasi e-commerce untuk peralatan olahraga.

## Tautan Aplikasi
[https://fauzan-putra31-sportify.pbp.cs.ui.ac.id/](https://fauzan-putra31-sportify.pbp.cs.ui.ac.id/)

## Implementasi Checklist

1. Membuat proyek Django baru dengan perintah 
```
django-admin startproject sportify
```
2. Masuk ke direktori proyek sportify dan buat aplikasi baru dengan nama main
```
python manage.py startapp main
```
3. Mengatur routing di `sportify/urls.py` untuk mengarahkan ke aplikasi `main`.
4. Tambahkan aplikasi main ke INSTALLED_APPS di file settings.py dalam proyek Django.

4. Membuat model `Product` dengan atribut `name`, `image`, `price`, `stok`, dan `description`.
5. Jalankan migrasi untuk menerapkan perubahan ke database:
```
python manage.py makemigrations
python manage.py migrate
```
5. Membuat fungsi `show_main` di `views.py` untuk menampilkan nama aplikasi, nama,kelas, dan detail produk.
6. Mengatur routing di `main/urls.py`.
6. Buat folder templates di dalam direktori proyek dan tambahkan file HTML
6. Buat folder static di dalam direktori proyek dan tambahkan file CSS
6. Buat folder media di dalam direktori proyek dan tambahkan foto produk.
6. Hapus entri untuk media dari file .gitignore agar file media dapat di-push ke PWS.

8. Menjalankan `collectstatic` untuk mengumpulkan file static.
```
python manage.py collectstatic
```
7. Melakukan deployment ke PWS.

## Bagan Request-Response Django

![Bagan MVT](https://i.ibb.co.com/D7SscYc/URLS-urls-py-1.png)

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
