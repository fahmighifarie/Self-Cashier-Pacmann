import numpy as np
import pandas as pd
from money import Money
from tabulate import tabulate

class Transaction_123:
    
    def __init__(self):
        
        self.item = {'Nama Item': [], 'Jumlah': [], 'Harga Item': [],"Harga": []}
        print('Selamat Datang Di Savoring Merchandise')
        
    def tambah_barang(self):
        while (True):
            nama_item = str(input("Masukan nama item: "))
            if nama_item == 'selesai':
                break
            while True:
                try:
                    harga_per_item = int(input("Masukan harga item: "))
                    jumlah_item = int(input("Masukan jumlah item: ")) 
                    harga_total_item = harga_per_item*jumlah_item
                    break
                except ValueError:
                    print('format tidak sesuai, silakan ulangi lagi')                      
            self.item['Nama Item'].append(nama_item)
            self.item['Jumlah'].append(jumlah_item)
            self.item['Harga Item'].append(harga_per_item)
            self.item['Harga'].append(harga_total_item)
            df=pd.DataFrame(self.item)
        print(df)
        
    def update_nama(self):
        nama_item = input("Masukan nama item yang akan diganti: ")
        nama_item_baru = input("Masukan nama item yang baru: ")
        
        if nama_item not in self.item["Nama Item"]:
            print("Item yang anda masukan tidak tersedia")
        else:
            temp=self.item["Nama Item"].index(nama_item)
            self.item["Nama Item"][temp]=nama_item_baru
        df=pd.DataFrame(self.item)
        print(df)
    
    def update_harga (self):
        nama_item = input("Masukan nama item yang akan diganti harganya: ")
        harga_baru = input("Masukan harga item baru: ")
        
        if nama_item not in self.item["Nama Item"]:
            print("Item yang anda masukan tidak tersedia")
        else:
            temp=self.item["Nama Item"].index(nama_item)
            self.item["Harga Item"][temp]=harga_baru
        df=pd.DataFrame(self.item)
        print(df)
    
    def update_jumlah (self):
        nama_item = input("Masukan nama item yang akan diganti jumlahnya: ")
        jumlah_baru = input("Masukan jumlah item baru: ")
        
        if nama_item not in self.item["Nama Item"]:
            print("Item yang anda masukan tidak tersedia")
        else:
            temp=self.item["Nama Item"].index(nama_item)
            self.item["Jumlah"][temp]=jumlah_baru
        df=pd.DataFrame(self.item)
        print(df)
    
    def delete (self):
        nama_item = input("Masukan nama item yang akan dihapus ")
        if nama_item not in self.item["Nama Item"]:
            print("Item yang anda masukan tidak tersedia")
        else:
            temp=self.item["Nama Item"].index(nama_item)
            for i in self.item:
                self.item[i].pop(temp)
        df=pd.DataFrame(self.item)
        print(df)
    
    def reset(self):
        batal=("Apakah ingin membatalkan semua pesanan? (y/n)").lower()
        if batal == "y":
            self.item.clear()
            print("Transaksi Dibatalkan")
            df=pd.DataFrame(self.item)
            print(df)
    
    def check_out(self):
        while True:
            try:
                periksa = input("Apakah akan lanjut check out? (lanjut/tidak)")
                if periksa == "lanjut":
                    df=pd.DataFrame(self.item)
                    print(df)
                    break
            except:
                continue

    def harga_total(self):
        total_harga = sum(self.item["Harga"])
        harga_diskon = 0
        
        if total_harga > 500_000:
            harga_diskon = total_harga-(total_harga*0.1)
            print(f"Total Belanja Anda Sebesar: {total_harga}")
            print("Anda Mendapatkan Diskon Sebesar 10%")
            print(f"nilai yang harus anda bayar adalah Rp. {harga_diskon},-")
            
        elif total_harga > 300_000:
            harga_diskon = total_harga-(total_harga*0.08)
            print(f"Total Belanja Anda Sebesar: {total_harga}")
            print("Anda Mendapatkan Diskon Sebesar 8%")
            print(f"nilai yang harus anda bayar adalah Rp. {harga_diskon},-")
            
        elif total_harga > 200_000:
            harga_diskon = total_harga-(total_harga*0.05)
            print(f"Total Belanja Anda Sebesar: {total_harga}")
            print("Anda Mendapatkan Diskon Sebesar 5%")
            print(f"nilai yang harus anda bayar adalah Rp. {harga_diskon},-")
            
        else:
            print(f"Total Belanja Anda Sebesar: {total_harga}")
            print(f"nilai yang harus anda bayar adalah Rp. {total_harga},-")


