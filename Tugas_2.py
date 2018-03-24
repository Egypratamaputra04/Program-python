jawab = "Y"
no = 0
Nama = []
Nim = []
Nilai_Tugas = []
Nilai_Uts = []
Nilai_Uas = []
while( jawab == "Y"):
    Nama.append(input("Nama :"))
    Nim.append(input("Nim :"))
    Nilai_Tugas.append(input("Nilai Tugas :"))
    Nilai_Uts.append(input("Nilai Uts :"))
    Nilai_Uas.append(input("Nilai Uas :"))
    jawab = input ("Tambah Data (Y/T)?")
    no += 1
print("=======================================================================")
print("| No | Nama | Nim | Nilai Tugas | Nilai Uts | Nilai Uas | Nilai Akhir |")
print("=======================================================================")
for n in range(no):
    NT = int(Nilai_Tugas[n])
    NU = int(Nilai_Uts[n])
    NA = int(Nilai_Uas[n])
    Akhir = (NT*30/100) + (NU*35/100) + (NA*35/100)
    print("| {} | {}    | {}    | {}    | {}    | {}    | {}   |".format(n+1,Nama[n],Nim[n],Nilai_Tugas[n],Nilai_Uts[n],Nilai_Uas[n],Akhir))
