print("========= PROGRAM NILAI KELAS X-PPLG ===========")

nilai =int(input("input berapa nilai?     "))
ratakel = 0
for i in range(1, nilai+1):
    print (i)
    nama = input("nama siswa :   ")
    tugas = float(input("nilai tugas :    "))
    harian = float(input("nilai harian :    "))
    pts = float(input("nilai pts :     "))
    pas = float(input("nilai pas :    "))
    jumlah = tugas + harian + pts + pas
    print(jumlah)
    rata = jumlah / 4
    print(rata)
    print()
    ratakel += rata
    print ("rata-rata kelas",ratakel / nilai)\

