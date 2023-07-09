# PYTHON PROJECT KASIR MANDIRI
Fahmi Ghifarie

## Latar Belakang
Sistem kasir mandiri ini dibuat untuk memenuhi tugas akhir dalam kelas Python I dan Python II dari Pacmann. 
Ide membuat project kasir mandiri diri dikarenakan kebutuhan dari seorang pemilik toko yang dimana ingin mengurangi kekeliruan para kasir yang menghitung pembayaran secara manual karena kecerobohan ini disebkan beberapa hal yang pertama adalah kurangnya jumlah karyawan yang dapat meng-handle transaksi kedua semakin lama karyawan bekerja biasanya konsentrasi para karyawan akan menurun. Maka dari itu dibuatkan sistem kasir mandiri ini agar pembeli dapat secara langsung menambahkan item yang dibeli, mengubah harga item yang dibeli dan mengubah jumlah item yang dibeli juga sekaligus dapat menjalankan total biaya yang harus didapatkan dan beberapa diskon menarik di dalamnya.

## Fitur/Requirements
- Class `Transaksi_123` untuk menghimpun seluruh kegiatan kasir mandiri
- Membuat fungsi `tambah_barang` untuk menambahkan barang
- Membuat fungsi `update_nama` untuk mengganti nama barang
- Membuat fungsi `update_harga` untuk mengganti harga barang
- Membuat fungsi `update_jumlah` untuk mengganti jumlah barang
- Membuat fungsi `delete` untuk menghapus barang
- Membuat fungsi `reset` untuk me-reset transaksi
- Membuat fungsi `check_out` untuk menampilkan belanja
- Membuat fungsi `harga_total` untuk menghitung total semua belanja

## Flowchart
![Flowchart Diagram](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/958e1d18-0224-4ec4-b36a-748d5260b563)

### Method
- `__init__(self)`. Menginisiasi variable utama pada sebuah class. Dalam hal ini adalah variable `self.item = {'Nama Item': [], 'Jumlah': [], 'Harga Item': [],"Harga": []}` yang dinisiasi.
- `tambah_barang()`. Fungsi ini dipanggil untuk menambahkan barang dimana setiap masukan dihimpun di suatu dictionary -> `self.item = {'Nama Item': [], 'Jumlah': [], 'Harga Item': [],"Harga": []}`
- `update_nama()`. Fungsi ini dipanggil untuk mengganti `nama_item` dimana `nama_item` yang akan diganti harus diinput terlebih dulu lalu akan keluar perintah input untuk memasukan `nama_item_baru`.
- `update_harga()`. Mengganti harga per item barang jika barang yang disebutkan tersedia dengan masukan yang diminta adalah `nama_item` lalu input `harga_baru`
- `update_jumlah()`. Mengganti jumlah pesanan barang jika barang yang disebutkan tersedia dengan masukan yang diminta adalah `nama_item` lalu input `jumlah_baru`
- `delete()`. Mengapus satu item dari `self.item` dengan masukan `nama_item`
- `reset()`. Mengosongkan semua barang sekaligus yang telah ditambahkan.
- `check_out()`. Menampilkan semua item yang sudah dimasukan ke `self.item` tujuannya untuk mengecek ulang item yang sudah dibeli 
- `harga_total`. Menampilkan seluruh barang beserta total harga tiap barang, discount, dan total setelah diskon.
- `__init__`. Menginisiasi variable utama pada sebuah class. Dalam hal ini adalah variable `items` yang dinisiasi.
- Ketentuan harga diskon adalah sebagai berikut:
	1. Jika di atas Rp 200.000 diskon sebesar 5%
	2. Jika di atas Rp 300.000 diskon sebesar 8%
	3. Jika di atas Rp 500.000 diskon sebesar 10%

## Contoh Pengujian
Pengujian dijalankan pada modul `testcase.py` dimana pada modul `testcase.py` ini memanggil modul `modulkasir.py`. Lalu diboatkan object menggunakan `transaksi1 = Transaksi_123()`. Untuk contoh dapat dilihat sebagai berikut: 

![contoh_pengujian](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/99090a14-4cda-4fa4-8648-bfe1635e1b09)

### Test 1: tambang_barang()
Customer ingin menambahkan tiga item baru menggunakan method `tambang_barang()`. 
![tambah_barang()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/962a881a-e05f-4f2b-9cfc-9b50b08fa9e5)
![image](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/318dd601-a76d-49f9-92dc-0580ab5f6a1a)

### Test 2: delete_item()
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggukan method `delete()` untuk menghapus item. Item yang ingin dihapuskan adalah `nama_item` yang sudah terdaftar di pemesanan sebelumnya.
![delete()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/6793c7a4-b7a9-479f-8f8c-03b1980fd8ad)
![delete() output](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/f527accd-7a7b-4137-bbdf-7a924e065e8a)

### Test 3: reset_transaction()
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu - satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

**Output:**
![968e3200-3384-4b00-908c-408cdf120261](https://user-images.githubusercontent.com/24706517/210151004-7595102c-2295-4c95-aa2b-d371ee05f86b.png)


### Test 4: total_price_print()
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `total_price_print()`. Sebelum mengeluarkan output total belanja akan menampilkan item - item yang dibeli. Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

**Output:**
![af6367f8-fc1b-4812-8737-61371bd02cab](https://user-images.githubusercontent.com/24706517/210151020-c3fa620b-f6ad-4daa-8585-ca674e7bf5ab.png)
![88d2953e-9810-44fd-8079-f9ccbdf82d5e](https://user-images.githubusercontent.com/24706517/210151025-119c5f17-9b46-4753-9791-073efe76f673.png)
![b0120508-12f2-4a94-a756-8b575d4fc43c](https://user-images.githubusercontent.com/24706517/210151035-85c815ce-e420-4000-8891-e1407219fa50.png)

### Test 5: update_nama()
Customer ingin mengganti nama **celana** yang terlanjur ditambahkan menggunakan metode `update_name()` sehingga nama item tersebut menjadi **kaos**

**Output:**
![f97c103c-8ef9-4151-bb91-f0433c0b7d87](https://user-images.githubusercontent.com/24706517/210151089-3ff9bcd4-6b70-4eeb-a132-8516163b8d73.png)
_Setelah nama diupdate_
![aa4e06d1-295b-4094-ad3f-3b1d522b8d10](https://user-images.githubusercontent.com/24706517/210151096-a6526741-3654-48ed-8f8b-03592630462a.png)


### Test 6: update_item_qty()
Customer ingin mengganti Quantity dari **Ayam Goreng Balado** yang sebelumnya 2 buah menjadi 10 buah dengan metode `update_item_qty()`

**Output:**
![3a2f22d7-7f76-4bf0-8ef9-886f9d411e75](https://user-images.githubusercontent.com/24706517/210151107-ad15c629-ee50-4117-81b1-71a114647466.png)
_Setelah qty diupdate_
![df029b88-1602-440c-85b8-567e5a8f6724](https://user-images.githubusercontent.com/24706517/210151112-0cdbbe87-1dad-491e-8add-1dc2558a3ee7.png)

### Test 7: update_harga()
Customer ingin mengganti harga per item dari **kaos** yang sebelumnya 160000 menjadi 75000 per item-nya dengan metode `update_harga()`.

![update_harga()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/a6371a5d-bc33-4735-9b68-8083fce5bca5)
![update_harga() ss](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/60c3c120-7c94-496e-9d80-4381c25398e8)



**Output**:
![df029b88-1602-440c-85b8-567e5a8f6724](https://user-images.githubusercontent.com/24706517/210151119-8ff07d98-9a3e-4898-8c3d-340e39dc7226.png)
_Setelah harga diupdate_
![21169f22-9f74-4902-a162-dc2d7ddb1a69](https://user-images.githubusercontent.com/24706517/210151124-e7e08787-210d-4372-a462-c21b977b6e17.png)


## Kesimpulan
- Super cashier adalah program sederhana yang membantu penjual untuk menjual produknya secara efektif dan efisien.
- Terdapat fitur menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan menjumlahkan keseluruhan harga barang beserta diskonnya secara cepat dan tepat.
- Keseluruhan fitur tersebut dapat memudahkan dan mempercepat pembeli untuk membeli barangnya secara mandiri.

## Future Work
- Membuat GUI (_Graphical User Interface_)
- Membuat sistem pembayaran yang terintegrasi dengan sistem kasir
