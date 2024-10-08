# Input
hrg = float(input("Masukkan harga per kg mangga (Rp): "))  # harga per kg
brt = float(input("Masukkan berat pembelian mangga (kg): "))  # berat pembelian

# Proses
byr = hrg * brt  # total harga yang harus dibayar

# Output
print(f"Total harga yang harus dibayar: Rp {byr:.2f}")
