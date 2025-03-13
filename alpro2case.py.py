import time
import random

class PencarianProduk:
    def __init__(self):
        # Simulasi database produk (dalam kasus nyata, ini akan terhubung ke database)
        self.produk = []
        self.produk_terindex = {}
        
    def generate_data(self, jumlah=20):
        """Membuat data produk acak untuk simulasi"""
        categories = ["Elektronik", "Fashion", "Kesehatan", "Rumah Tangga", "Otomotif"]
        nama_produk = [
            "Smartphone X10", "Laptop Pro", "Kemeja Formal", "Sepatu Running", 
            "Vitamin C", "Panci Elektrik", "Helm Motor", "Bola Basket", 
            "Mainan Puzzle", "Kue Kering", "Keyboard Gaming", "Charger Wireless", 
            "Dress Casual", "Celana Jeans", "Obat Flu", "Blender", 
            "Oli Mesin", "Raket Badminton", "Komik", "Headphone"
        ]
        
        print(f"Membuat {jumlah} produk untuk simulasi...")
        start_time = time.time()
        
        # Reset data
        self.produk = []
        self.produk_terindex = {}
        
        # Generate data dengan jumlah terbatas
        max_produk = min(jumlah, len(nama_produk))
        
        for i in range(max_produk):
            id_produk = i + 1
            nama = nama_produk[i]
            kategori = random.choice(categories)
            harga = random.randint(10000, 10000000)
            rating = round(random.uniform(1, 5), 1)
            
            produk = {
                "id": id_produk,
                "nama": nama,
                "kategori": kategori,
                "harga": harga,
                "rating": rating
            }
            
            self.produk.append(produk)
            
            # Buat index untuk solusi baik
            if kategori not in self.produk_terindex:
                self.produk_terindex[kategori] = []
            self.produk_terindex[kategori].append(produk)
        
        elapsed_time = time.time() - start_time
        print(f"Data berhasil dibuat dalam {elapsed_time:.6f} detik")
        
        # Tampilkan semua produk yang dibuat
        print("\nDaftar Produk yang Dibuat:")
        print("=" * 80)
        print(f"{'ID':<4} {'Nama':<20} {'Kategori':<15} {'Harga':<15} {'Rating':<6}")
        print("-" * 80)
        
        for produk in self.produk:
            harga_format = f"Rp {produk['harga']:,}"
            print(f"{produk['id']:<4} {produk['nama']:<20} {produk['kategori']:<15} {harga_format:<15} {produk['rating']:<6}")
            
        print("=" * 80)
        
        # Tampilkan statistik kategori
        print("\nStatistik Kategori:")
        for kategori, produk_list in self.produk_terindex.items():
            print(f"{kategori}: {len(produk_list)} produk")
        
    def cari_produk_buruk(self, kategori, min_rating=0):
        """
        Mencari produk berdasarkan kategori dengan metode linear search
        Kompleksitas: O(n) - harus mengecek setiap produk
        """
        print("\n--- MENCARI DENGAN ALGORITMA BURUK (LINEAR SEARCH O(n)) ---")
        
        # Timer mulai
        start_time = time.time()
        hasil = []
        
        # Linear search - memeriksa setiap produk satu per satu
        for produk in self.produk:
            # Simulasi delay untuk menunjukkan perbedaan performa lebih jelas
            time.sleep(0.1)  # Delay 100ms per produk untuk simulasi
            
            if produk["kategori"] == kategori and produk["rating"] >= min_rating:
                hasil.append(produk)
                
        # Timer selesai
        elapsed_time = time.time() - start_time
        
        # Tampilkan hasil
        self._tampilkan_hasil(hasil, elapsed_time)
        
        return elapsed_time
    
    def cari_produk_baik(self, kategori, min_rating=0):
        """
        Mencari produk berdasarkan kategori dengan metode indexed search
        Kompleksitas: O(1) untuk akses kategori + O(m) untuk filter rating
        di mana m adalah jumlah produk dalam kategori (biasanya m << n)
        """
        print("\n--- MENCARI DENGAN ALGORITMA BAIK (INDEXED SEARCH O(1) + O(m)) ---")
        
        # Timer mulai
        start_time = time.time()
        hasil = []
        
        # Indexed search - langsung mengakses produk dengan kategori yang diinginkan
        if kategori in self.produk_terindex:
            for produk in self.produk_terindex[kategori]:
                # Simulasi delay untuk setiap produk yang diperiksa dalam kategori
                time.sleep(0.1)  # Delay 100ms per produk untuk simulasi
                
                if produk["rating"] >= min_rating:
                    hasil.append(produk)
        
        # Timer selesai
        elapsed_time = time.time() - start_time
        
        # Tampilkan hasil
        self._tampilkan_hasil(hasil, elapsed_time)
        
        return elapsed_time
    
    def _tampilkan_hasil(self, hasil, waktu):
        """Menampilkan hasil pencarian dalam format sederhana"""
        print(f"\nMenemukan {len(hasil)} produk dalam {waktu:.6f} detik")
        
        if not hasil:
            print("Tidak ada produk yang ditemukan.")
            return
        
        # Tampilkan semua produk yang ditemukan
        print("\nHasil Pencarian:")
        print("=" * 80)
        print(f"{'ID':<4} {'Nama':<20} {'Kategori':<15} {'Harga':<15} {'Rating':<6}")
        print("-" * 80)
        
        for produk in hasil:
            harga_format = f"Rp {produk['harga']:,}"
            print(f"{produk['id']:<4} {produk['nama']:<20} {produk['kategori']:<15} {harga_format:<15} {produk['rating']:<6}")
            
        print("=" * 80)
    
    def perbandingan(self, kategori, min_rating=0):
        """Membandingkan performa kedua algoritma"""
        print("\n=== PERBANDINGAN ALGORITMA PENCARIAN ===")
        
        # Jalankan kedua algoritma
        waktu_buruk = self.cari_produk_buruk(kategori, min_rating)
        waktu_baik = self.cari_produk_baik(kategori, min_rating)
        
        # Tampilkan perbandingan
        print("\n--- HASIL PERBANDINGAN ---")
        print("=" * 80)
        print(f"{'Algoritma':<30} {'Waktu Eksekusi':<20} {'Kompleksitas':<15} {'Kecepatan':<15}")
        print("-" * 80)
        
        speedup = waktu_buruk / waktu_baik if waktu_baik > 0 else float('inf')
        
        print(f"{'Linear Search (Buruk)':<30} {waktu_buruk:.6f} detik{'':<8} {'O(n)':<15} {'1x':<15}")
        print(f"{'Indexed Search (Baik)':<30} {waktu_baik:.6f} detik{'':<8} {'O(1) + O(m)':<15} {speedup:.2f}x lebih cepat")
        print("=" * 80)
        
        print("\nKesimpulan:")
        print(f"Algoritma Indexed Search {speedup:.2f}x lebih cepat dari Linear Search untuk pencarian ini.")
        if speedup > 1:
            print(f"Ini terjadi karena Linear Search harus memeriksa semua {len(self.produk)} produk,")
            print(f"sementara Indexed Search hanya perlu memeriksa produk dalam kategori '{kategori}'.")
        else:
            print("Untuk jumlah data yang kecil, perbedaan mungkin tidak signifikan.")


# Contoh penggunaan
if __name__ == "__main__":
    import sys
    
    pencarian = PencarianProduk()
    
    # Generate data produk (default 20)
    jumlah_data = 20
    pencarian.generate_data(jumlah_data)
    
    while True:
        print("\n=========================================")
        print("SIMULASI PENCARIAN PRODUK BUKALAPAK")
        print("=========================================")
        print("1. Cari dengan Solusi Buruk O(n)")
        print("2. Cari dengan Solusi Baik O(1)+O(m)")
        print("3. Bandingkan Kedua Solusi")
        print("4. Keluar")
        
        pilihan = input("\nPilih opsi (1-4): ")
        
        if pilihan == "1" or pilihan == "2" or pilihan == "3":
            kategori = input("Masukkan kategori produk (Elektronik, Fashion, Kesehatan, Rumah Tangga, Otomotif): ")
            min_rating = input("Masukkan rating minimum (1-5): ")
            
            try:
                min_rating = float(min_rating)
                if not (1 <= min_rating <= 5):
                    raise ValueError
            except ValueError:
                min_rating = 0
                print("Rating tidak valid, menggunakan default (tanpa filter rating)")
            
            if pilihan == "1":
                pencarian.cari_produk_buruk(kategori, min_rating)
            elif pilihan == "2":
                pencarian.cari_produk_baik(kategori, min_rating)
            else:
                pencarian.perbandingan(kategori, min_rating)
                
        elif pilihan == "4":
            print("Terima kasih telah menggunakan simulasi pencarian produk!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")