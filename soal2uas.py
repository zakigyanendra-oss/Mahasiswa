FILE_NAME = "mahasiswa.txt"


def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    prodi = input("Masukkan Program Studi: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{nim}|{nama}|{prodi}\n")

    print("Data mahasiswa berhasil ditambahkan.")


def tampilkan_mahasiswa():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

        if not data:
            print("Data mahasiswa masih kosong.")
            return

        print("===== DAFTAR MAHASISWA =====")
        for i, line in enumerate(data, start=1):
            nim, nama, prodi = line.strip().split("|")
            print(f"{i}. NIM   : {nim}")
            print(f"   Nama  : {nama}")
            print(f"   Prodi : {prodi}")
            print("---------------------------")

    except FileNotFoundError:
        print("Data mahasiswa masih kosong.")


def cari_mahasiswa():
    nim_cari = input("Masukkan NIM yang dicari: ")

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                nim, nama, prodi = line.strip().split("|")
                if nim == nim_cari:
                    print("Data mahasiswa ditemukan:")
                    print("NIM   :", nim)
                    print("Nama  :", nama)
                    print("Prodi :", prodi)
                    return

        print("Data mahasiswa tidak ditemukan.")

    except FileNotFoundError:
        print("Data mahasiswa masih kosong.")


def hapus_mahasiswa():
    nim_hapus = input("Masukkan NIM yang akan dihapus: ")

    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

        with open(FILE_NAME, "w") as file:
            ditemukan = False
            for line in data:
                nim, nama, prodi = line.strip().split("|")
                if nim != nim_hapus:
                    file.write(line)
                else:
                    ditemukan = True

        if ditemukan:
            print("Data mahasiswa berhasil dihapus.")
        else:
            print("Data mahasiswa tidak ditemukan.")

    except FileNotFoundError:
        print("Data mahasiswa masih kosong.")


while True:
    print("===== MENU PENGELOLAAN MAHASISWA =====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa (NIM)")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan == "2":
        tampilkan_mahasiswa()
    elif pilihan == "3":
        cari_mahasiswa()
    elif pilihan == "4":
        hapus_mahasiswa()
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid!")

    print()