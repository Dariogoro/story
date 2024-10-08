# Diketahui
print("Diketahui:")
brt = 5  # berat telur dalam kilogram
hrg = 26000  # harga per kilogram telur
ongkos = 3500 * 2  # ongkos pulang pergi (3500 sekali naik)
uang = 200000  # uang yang dibawa ibu

# Menampilkan informasi yang diketahui
print(f"1. Berat telur = {brt} kg")
print(f"2. Harga telur per kg = Rp {hrg}")
print(f"3. Ongkos transport PP = Rp {ongkos}")
print(f"4. Uang yang dibawa ibu = Rp {uang}")

# Cara Pengerjaan
print("\nCara Pengerjaan:")
print("1. Hitung total biaya telur:")
print(f"   Total biaya telur = Berat telur * Harga per kg = {brt} * {hrg} = Rp {brt * hrg}")
print("2. Hitung total biaya keseluruhan:")
print(f"   Total biaya = Total biaya telur + Ongkos = Rp {brt * hrg} + Rp {ongkos} = Rp {brt * hrg + ongkos}")
print("3. Hitung sisa uang:")
print(f"   Sisa uang = Uang yang dibawa ibu - Total biaya = Rp {uang} - Rp {brt * hrg + ongkos}")

# Hitung total biaya telur
total_telor = brt * hrg

# Hitung total biaya
total_biaya = total_telor + ongkos

# Hitung sisa uang
sisa = uang - total_biaya

# Output
print("\nSisa uang ibu adalah Rp", sisa)

