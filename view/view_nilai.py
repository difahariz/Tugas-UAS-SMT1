print("--------------------------------")
selected_menu = input("Pilih menu> ")
print("Ketik (L) untuk Menampilkan Data")

if selected_menu == "L":
    if x.items():
        print("=" * 74)
        print("|                            Daftar Mahasiswa                            |")
        print("=" * 74)
        print("| No |     Nama        |     NIM     |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("=" * 74)
        i = 0
        for z in x.items():
            i += 1
            print("| {no:^2} | {0:15} | {1:^11d} | {2:^5d} | {3:^5d} | {4:^7d} | {5:^7.2f} |"
                  .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
        print("=" * 74)
    else:
        print("=" * 73)
        print("|                             Daftar Mahasiswa                          |")
        print("=" * 73)
        print("|         Nama         |    NIM    |  UTS  |  UAS  |  Tugas  |   Akhir  |")
        print("=" * 73)
        print("|                             TIDAK ADA DATA                            |")
        print("=" * 73)
    print()