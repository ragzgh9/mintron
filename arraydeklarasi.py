array = []
Total = 0
n = int (input("Masukkan Jumlah elemen array "))
for x in range(n):
    nilai = float(input("Masukkan nilai ke- {} :". format(x+1)))
    array.append(nilai)
print("\nHasil nilai total adalah :  {}".format(sum(array)))
print("Hasil Rata-Rata Adalah :  {}".format(sum(array)/n))