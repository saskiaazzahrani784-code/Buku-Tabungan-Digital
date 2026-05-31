saldo = 0

while True:
    print("\n===== BUKU TABUNGAN DIGITAL =====")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Saldo")
    print("4. Keluar")

    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        pemasukan = int(input("Masukkan jumlah pemasukan: Rp "))
        saldo += pemasukan
        print("Pemasukan berhasil ditambahkan.")

    elif choice == "2":
        pengeluaran = int(input("Masukkan jumlah pengeluaran: Rp "))

        if pengeluaran > saldo:
            print("Saldo tidak mencukupi.")
        else:
            saldo -= pengeluaran
            print("Pengeluaran berhasil dicatat.")

    elif choice == "3":
        print("Saldo saat ini: Rp", saldo)

    elif choice == "4":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Masukkan angka 1 sampai 4.")
