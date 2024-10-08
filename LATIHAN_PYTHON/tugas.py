nama=input("Nama: ")
nim=input("NIM : ")
kelas=input("Kelas : ")

nomor1 = input("Masukan Aksi Pertama: ")
nomor2 = input("Masukan Aksi Kedua: ")
variable = input("Masukan Perintah(+, -, *, /): ")

tambah = float(nomor1) + float(nomor2)
kurang = float(nomor1) - float(nomor2)
kali = float(nomor1) * float(nomor2)
bagi = float(nomor1) / float(nomor2)

if variable == "+":
    print ("Hasil: "+str(tambah))

elif variable == "-":
    print ("Hasil: "+str(kurang))

elif variable == "*":
   print ("Hasil: "+str(kali))

elif variable == "/":
    print ("Hasil: "+str(bagi))

else:
    print("Error: Invalid")