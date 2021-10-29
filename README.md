# Ecommerce Checkout Problem

Ini adalah PoC dari masalah "eCommerce Checkout Problem"
dimana user mendapatkan situasi barang yang mereka akan beli harus di batalkan oleh pihak eCommerce karena ternyata ketersediaan produk sudah tidak ada.

## What Happened?
User melakukan checkout terhadap order yang didalamnya terdapat produk / item yang ternyata jumlah stoknya sudah habis pada sistem. Karena jumlah stok yang terdapat pada sistem salah, hal ini membuat user masih bisa melakukan checkout terhadap produk tersebut. Hal tersebut bisa terjadi karena penyebab berikut:

### Penyebab 1: 
Terdapat kesalahan pada proses pencatatan stok terakhir produk ketika ada proses checkout secara bersamaan. 

Dari level database, hal ini bisa terjadi ketika terdapat dua entitas yang berusaha melakukan update terhadap sebuah field pada record yang sama di database secara bersamaan. 

### Penyebab 2:
Ketika banyaknya proses transaksi pada database tanpa adanya validasi terlebih dahulu terhadap jumlah stok ketika user melakukan checkout.

Dari level aplikasi, bisa saja terdapat kesalahan update jumlah stok ketika proses checkout dilakukan, dimana seharusnya sebelum proses checkout / pembayaran dilakukan proses pengecekan terhadap jumlah stok produk telebih dahulu. Jika pada saat proses checkout ternyata stok produk sudah habis, proses checkout akan gagal. Jika ternyata stok produk masih tersedia proses checkout bisa dilakukan.

## Proposed Solution
Solusi yang dapat dilakukan untuk menanggulangi proses tersebut sebagai berikut:

- Membuat endpoint API untuk proses pengecekan jumlah stok barang, atau bisa juga pada endpoint checkout / pembayaran dilakukan proses pengecekan stok barang terlebih dahulu sebelum memproses checkout / pembayaran.  

- Membuat field "version" pada table stok produk. Ketika akan mengupdate jumlah stok produk, field version harus di update juga untuk menghindari proses "conflict" jika terdapat lebih dari satu proses transaksi update pada database.

## Docs
### ERD
![alt text](https://drive.google.com/uc?export=view&id=1fRJIZ2O1h4hey_1X_9NzKeOoaI23sskx)


## Installation
This project requires [Python] (https://www.python.org/) 3.8+ to run.

- Install pip
- Install and create virtualenv
  ```sh
  pip install virtualenv
  virtualenv venv
  ```
- Install the project dependecies
  ```sh
  pip install -r requirements.txt
  ```
- Activate the virtualenv
  Linux:
  ```sh
    source venv/bin/activate
  ```
  Windows:
  ```sh
    .\venv\Scripts\activate
  ```
- Copy the .env.example file
- Start the ASGI Server using uvicorn
  ```sh
  uvicorn main:app --reload --host 127.0.0.1 --port 8080
  ```
