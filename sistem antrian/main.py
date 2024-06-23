import csv
from tabulate import tabulate

class Antrian:
    def __init__(self):
        self.items = []
        self.load_from_csv()  # Memuat data antrian dari file CSV saat inisialisasi
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        if len(self.items) < 20:  # Batas maksimal 5 pasien
            self.items.append(item)
            self.save_to_csv()  # Simpan data ke file CSV setelah enqueue
            print(f"Pasien {item} telah ditambahkan ke dalam antrean.")
        else:
            print("Antrian Sudah Penuh")
    
    def dequeue(self):
        if not self.is_empty():
            item = self.items.pop(0)
            self.save_to_csv()  # Simpan data ke file CSV setelah dequeue
            return item
        else:
            print("Antrian kosong.")
    
    def update_pasien(self, index, nama_baru):
        if 0 <= index < len(self.items):
            self.items[index] = nama_baru
            self.save_to_csv()  # Simpan data ke file CSV setelah update
            print(f"Data pasien pada indeks {index} berhasil diperbarui.")
        else:
            print("Indeks pasien tidak valid.")
    
    def delete_pasien(self, index):
        if 0 <= index < len(self.items):
            removed_item = self.items.pop(index)
            self.save_to_csv()  # Simpan data ke file CSV setelah delete
            print(f"Pasien {removed_item} pada indeks {index} telah dihapus dari antrean.")
        else:
            print("Indeks pasien tidak valid.")
    
    def save_to_csv(self):
        with open('antrian.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.items)
    
    def load_from_csv(self):
        try:
            with open('antrian.csv', mode='r') as file:
                reader = csv.reader(file)
                self.items = next(reader, [])
        except FileNotFoundError:
            self.items = []  # Jika file tidak ditemukan, inisialisasi antrian kosong

class RumahSakit:
    def __init__(self):
        self.antrian = Antrian()
    
    def tambah_pasien(self, nama):
        self.antrian.enqueue(nama)
        print(" ")
    
    def panggil_pasien(self):
        pasien = self.antrian.dequeue()
        if pasien:
            print(f"Panggilan: Silakan masuk atas nama, {pasien}!")
            print(" ")
    
    def lihat_pasien(self):
        if not self.antrian.is_empty():
            table = []
            for i, pasien in enumerate(self.antrian.items):
                table.append([i, pasien])
            print(tabulate(table, headers=['No', 'Nama Pasien'], tablefmt='grid'))
            print(" ")
        else:
            print("Antrian kosong.")
            print(" ")
    
    def update_pasien(self, index, nama_baru):
        self.antrian.update_pasien(index, nama_baru)
        print(" ")
    
    def hapus_pasien(self, index):
        self.antrian.delete_pasien(index)
        print(" ")

# Membuat objek RumahSakit
rs = RumahSakit()

# Tampilan Menu dan input
while True:
    print("=========================================================")
    print("=         Sistem Antrian Berobat di Rumah Sakit         =")
    print("=========================================================")
    print("=    1. Tambah Pasien                                   =")
    print("=    2. Panggil Pasien                                  =")
    print("=    3. Lihat Daftar Pasien                             =")
    print("=    4. Perbarui Data Pasien                            =")
    print("=    5. Hapus Pasien                                    =")
    print("=    0. Keluar                                          =")
    print("=========================================================")
    print(" ")

    pilihan = input("Masukkan pilihan 1/2/3/4/5/0 :")
    print(" ")

    if pilihan == "1":
        nama_pasien = input("Masukkan nama pasien: ")
        rs.tambah_pasien(nama_pasien)
    elif pilihan == "2":
        rs.panggil_pasien()
    elif pilihan == "3":
        rs.lihat_pasien()
    elif pilihan == "4":
        index = int(input("Masukkan indeks pasien yang ingin diperbarui: "))
        nama_baru = input("Masukkan nama baru pasien: ")
        rs.update_pasien(index, nama_baru)
    elif pilihan == "5":
        index = int(input("Masukkan indeks pasien yang ingin dihapus: "))
        rs.hapus_pasien(index)
    elif pilihan == "0":
        print("Menyimpan data antrian...")
        break
    else:
        print("Pilihan yang anda masukan salah. Silakan coba lagi.")
