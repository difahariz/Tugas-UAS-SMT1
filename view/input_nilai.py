Menginput data

list_nama = []
list_nim = []
list_uts = []
list_tugas = []
list_uas = []
rata = []

a = 0
while True:
    list_nama.append(str(input("Masukan Nama\t\t : ")))
    list_nim.append(int(input("Masukan NIM\t\t : ")))
    tugas = int(input("Masukan Nilai Tugas\t : "))
    list_tugas.append(tugas)
    uts = int(input("Masukan Nilai UTS\t : "))
    list_uts.append(uts)
    uas = int(input("Masukan Nilai UAS\t : "))
    list_uas.append(uas)
    rata.append(tugas * 30/100 + uts * 35/100 + uas * 35/100)
    n = input("Lanjut (Y/T)\t\t : ")
    if n == "t" or n == "T":
        break
print ()

print (68*"=")
print("| {0:^3} | {1:^12} | {2:^9} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("NO", "NAMA", "NIM" , "TUGAS", "UTS", "UAS", "AKHIR"))
print (68*"=")

no = 0
for nama, nim, tugas, uts, uas, akhir in zip (list_nama, list_nim, list_tugas, list_uts, list_uas, rata):
    no += 1
    print ("| {0:>3} | {1:<12} | {2:>9} | {3:>5} | {4:>5} | {5:>5} | {6:>7} |".format(no, nama, nim, tugas, uts, uas, akhir))
print (68*"=")