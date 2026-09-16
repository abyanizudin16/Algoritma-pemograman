#Deskripsi Variabel
gelasA = "KOPI"
gelasB = "TEH"
gelasC = " "


print("=== Data Gelas Sebelum di Tukar===")
print("Gelas A :", gelasA)
print("Gelas B :", gelasB)
print("Gelas C :", gelasC)

#Proses penukaran menggunakan gelas C sebagai penampung sementara
gelasC = gelasA
gelasA = gelasB
gelasB = gelasC

#Gelas C dikosongkan
gelasC ="" 

#cetaknhasil setelah ditukar
print("\n==== Setelah Data ditukar ====")
print("Gelas A :", gelasA)
print("Gelas B :", gelasB)
print("Gelas C :", gelasC)