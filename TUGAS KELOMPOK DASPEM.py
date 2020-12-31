#KELOMOK 3
#Nama  Angota
#1.	Febby  Ivanda  Timbani
#2.	M.Panji  Irawan
#3.	Anyan
#4.	Yesinta  Pratiwi
#5.	Renaldy


#layar  masukan
print("	PALUGADA	")
print(" 	")
print("Kode	Jenis Sambal     Harga	") 
print("P	pedas	        Rp.35000")
print("M	manis	        Rp.35000")
print("B	balado	        Rp.35000")
print("A	asam	        Rp.40000")
print("                           	")

b_jenis =int(input("banyak jenis :"))
kode_sambal = []
banyak_sambal = []
jenis_sambal = []
harga = []
jumlah = []
i = 0
while i<b_jenis:
    print("jenis ke -",i+1)
    kode_sambal.append(input("kode sambal [P/M/B/A]:"))
    banyak_sambal.append(int(input("banyak sambal :")))

    if kode_sambal[i] == "P" or kode_sambal[i] == "p":
        jenis_sambal.append("pedas")
        harga.append("35000")
        jumlah.append(banyak_sambal[i]*int("35000"))
    elif kode_sambal[i] == "M" or kode_sambal[i] == "m":
        jenis_sambal.append("manis")
        harga.append("35000")
        jumlah.append(banyak_sambal[i]*int("35000"))
    elif kode_sambal[i] == "B" or kode_sambal[i] == "b":
        jenis_sambal.append("balado")
        harga.append("35000")
        jumlah.append(banyak_sambal[i]*int("35000"))
    elif kode_sambal[i] == "A" or kode_sambal[i] == "a":
        jenis_sambal.append("asam")
        harga.append("40000")
        jumlah.append(banyak_sambal[i]*int("40000"))
    else:
        jenis_sambal.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_sambal[i]*int("0"))
    i = i + 1

print("=======================================")
print("             PALUGADA                  ")
print("=======================================")
print("no       jenis   harga   banyak  jumlah")
print("         sambal  satuan  ambil   harga")
print("=======================================")

jumlah_bayar = 0
a = 0
while a < b_jenis:
    jumlah_bayar = jumlah_bayar + jumlah[a]
    print("%i   %s  %s  %i  %i" % (a+1,jenis_sambal[a],harga[a],banyak_sambal[a],jumlah[a]))
    a = a + 1

pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("                     pajak 10%   Rp:",pajak)
print("                     total bayar Rp:",total_bayar)