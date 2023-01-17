tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai uts: "))
uas = float(input("Masukkan nilai uas: "))


nilai = (0.15 + tugas) + (0.35 + uts) + (0.50 + uas)


if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'

if nilai > 60:
    status ='Lulus'
else:
    status = 'Tidak Lulus'

print('Nilai Akhir: %0.2f' % nilai)
print('Grade: {}'.format(grade))
print('Status: {}'.format(status))
