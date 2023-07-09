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


### Test 4: harga_total()
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method `harga_total()`. 

![harga_total()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/bb9e4933-55bc-47f9-b0bc-e9908428f276)
![ss_harga_total()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/a18b4d28-9570-4f33-bc75-a97a97aeb6eb)


### Test 5: update_nama()
Customer ingin mengganti nama **celana** yang terlanjur ditambahkan menggunakan metode `update_name()` sehingga nama item tersebut menjadi **kaos**

![update_nama()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/e52d33ae-5c8d-4eb7-86e2-58a197cb2f1a)
![ss_update_nama()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/a400f635-6d71-4e05-9407-028d077ed760)


### Test 6: update_jumlah()
Customer ingin mengganti Quantity dari **kaos** yang sebelumnya 1 buah menjadi 2 buah dengan metode `update_jumlah()`

![update_jumlah()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/6472933a-608b-48bb-9fa4-74ed1188bb14)
![ss_update)jumlah()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/34686eda-7667-4322-8355-dc780610e53e)



### Test 7: update_harga()
Customer ingin mengganti harga per item dari **kaos** yang sebelumnya 160000 menjadi 75000 per item-nya dengan metode `update_harga()`.

![update_harga()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/a6371a5d-bc33-4735-9b68-8083fce5bca5)
![update_harga() ss](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/60c3c120-7c94-496e-9d80-4381c25398e8)


### Test 8: check_out()
Customer ingin mmemastikan pesanan yang dibeli dengan dikeluarkan tampilan dengan menggunakan metode `check_out()`.

![checkout()](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/e2942ae2-403f-47e4-ace4-ee37d584c46d)
![ss_checkout](https://github.com/fahmighifarie/Self-Cashier-Pacmann/assets/68582818/b52789b1-5889-4eda-bbf0-c38a6a8a42e8)


## Kesimpulan
- Super cashier adalah program sederhana yang membantu penjual untuk menjual produknya secara efektif dan efisien.
- Terdapat fitur menambahkan barang, mengedit barang (nama, quantity, harga per item), menghapus barang, dan menjumlahkan keseluruhan harga barang beserta diskonnya secara cepat dan tepat.
- Keseluruhan fitur tersebut dapat memudahkan dan mempercepat pembeli untuk membeli barangnya secara mandiri.

## Future Work
- Membuat GUI (_Graphical User Interface_)
- Membuat sistem pembayaran yang terintegrasi dengan sistem kasir
