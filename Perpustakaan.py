print("=== Program Perpustakaan ===")

# Input ID Pengguna (hanya angka)
while True:
    try:
        id_user = int(input("Masukkan ID: "))
        break
    except:
        print("ID harus berupa angka!")

# Input Nama Pengguna (tanpa angka)
while True:
    nama = input("Masukkan Nama: ")
    if nama.isalpha():  # Cek apakah nama hanya berisi huruf
        break
    else:
        print("Nama tidak boleh mengandung angka atau karakter lain!")

# Input Username dan Password
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")

# Input Data Buku
nama_buku = input("Masukkan Nama Buku: ")

# Input Waktu Pinjaman (tahun, bulan, tanggal - hanya angka)
while True:
    try:
        tahun = int(input("Masukkan Tahun Pinjaman (contoh: 2024): "))
        break
    except:
        print("Tahun harus berupa angka!")

while True:
    try:
        bulan = int(input("Masukkan Bulan Pinjaman (contoh: 10): "))
        if 1 <= bulan <= 12:  # Cek apakah bulan valid
            break
        else:
            print("Bulan harus antara 1 hingga 12!")
    except:
        print("Bulan harus antara 1 hingga 12!")

while True:
    try:
        tanggal = int(input("Masukkan Tanggal Pinjaman (contoh: 8): "))
        if 1 <= tanggal <= 31:  # Cek apakah tanggal valid
            break
        else:
            print("Tanggal harus antara 1 hingga 31!")
    except:
        print("Tanggal harus antara 1 hingga 31!")

# Tambahkan durasi pinjaman (misalnya 7 hari)
durasi_pinjaman = 7
tanggal_balik = tanggal + durasi_pinjaman

# Handle ketika tanggal_balik melebihi jumlah hari dalam bulan (contoh sederhana tanpa kalender dinamis)
if tanggal_balik > 31:
    tanggal_balik = tanggal_balik - 31
    bulan += 1
    if bulan > 12:
        bulan = 1
        tahun += 1

# Format waktu pinjaman dan waktu balik
waktu_pinjaman = f"{tahun}-{str(bulan).zfill(2)}-{str(tanggal).zfill(2)}"
waktu_balik = f"{tahun}-{str(bulan).zfill(2)}-{str(tanggal_balik).zfill(2)}"

# Tampilkan Data Pengguna dan Peminjaman
print("\n=== Ringkasan Data Pengguna ===")
print(f"ID Pengguna : {id_user}")
print(f"Nama        : {nama}")
print(f"Username    : {username}")

print("\n--- Detail Peminjaman Buku ---")
print(f"Nama Buku      : {nama_buku}")
print(f"Waktu Pinjaman : {waktu_pinjaman}")
print(f"Waktu Balik    : {waktu_balik}")
