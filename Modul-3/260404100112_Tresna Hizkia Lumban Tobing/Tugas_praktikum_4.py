
jumlah_penuh = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
        print("\nKuota beasiswa penuh sudah terpenuhi.")
        break

    print("\nMahasiswa ke-", i)
    nama = input("Nama mahasiswa: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat.")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
    else:
        status = "Tidak mendapatkan beasiswa"

    print("Nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua: Rp", penghasilan)
    print("Hasil seleksi:", status)

if jumlah_penuh == 3:
    print("Kuota beasiswa penuh telah terpenuhi.")
else:
    print("Seleksi selesai.")

print("Jumlah penerima beasiswa penuh:", jumlah_penuh)