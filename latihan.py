print("=+=+=+=+ Data Diri Mahasiswa =+=+=+=+")
nim=input("Nim: ")
nama=input("Nama Lengkap : ")
jurusan=input("Jurusan : ")
alamat=input("Alamat : ")
uts=int(input("Nilai UTS : "))
uas=int(input("Nilai UAS : "))
total=(uts+uas)/2

print("")
print("Hasil cetak diatas adalah")
print("NIM : " +str(nim))
print("Nama : " +str(nama))
print("Jurusan : " +str(jurusan))
print("Alamat : " +str(alamat))
print("UTS : " +str(uts))
print("UAS : " +str(uas))
print("Nilai Akhir : " +str(total))
