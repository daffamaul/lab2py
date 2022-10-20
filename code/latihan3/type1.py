#input nilai variabel
a = input("masukkan nilai untuk a:")
b = input("masukkan nilai untuk b:")

#cetak nilai variabel
print("variabel a adalah ", a)
print("variabel b adalah ", b)

a = int(a)
b = int(b)
#cetak hasil operasi kedua variabel dengan string format
print("hasil penggabungan {1}&{0}=%d".format(a,b) %(a+b))

# konversi nilai variabel
a = int(a)
b = int(b)
print("hasil penjumlahan {1}+{0}=%d ".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}=%d ".format(a,b) %(a/b))