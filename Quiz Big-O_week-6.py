import time

class ShoppingCart:
    def __init__(self):
        self.total = 0  # Total harga belanja
        self.item_count = 0  # Jumlah barang
        self.start_time = time.time()  # Waktu mulai belanja

    def add_item(self, price):
        self.total += price  # Tambahkan harga ke total
        self.item_count += 1  # Tambahkan jumlah barang

    def get_total(self):
        return self.total

    def get_item_count(self):
        return self.item_count

    def get_shopping_duration(self):
        return time.time() - self.start_time  # Hitung durasi belanja

# Fungsi untuk menerima input dari pengguna
def main():
    cart = ShoppingCart()

    while True:
        try:
            # Minta input harga dari pengguna
            price = float(input("Masukkan harga barang (atau ketik '0' untuk selesai): "))
            
            # Jika pengguna memasukkan 0, keluar dari loop
            if price == 0:
                break
            
            # Tambahkan barang ke keranjang
            cart.add_item(price)
            print(f"Barang seharga {price} ditambahkan ke keranjang.")
        
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    # Tampilkan total belanja, jumlah barang, dan durasi belanja
    print("\n--- Ringkasan Belanja ---")
    print(f"Total belanja: {cart.get_total()}")
    print(f"Jumlah barang: {cart.get_item_count()}")
    print(f"Durasi belanja: {cart.get_shopping_duration():.2f} detik")

# Jalankan program
if __name__ == "__main__":
    main()