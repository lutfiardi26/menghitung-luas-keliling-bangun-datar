anggotaA = {1,2,3,4,5}
anggotaB = {5,6,7,8,9}

#mencetak Anggota Himpunan A dan Himpunan B
print("Anggota Himpunan A :")
print(anggotaA)
print("Anggota Himpunan B :")
print(anggotaB)
print("==============================================")

#operasi gabungan
gabungan = anggotaA.union(anggotaB)
print("Hasil Gabungan :")
print(gabungan)

#operasi irisan
irisan = anggotaA.intersection(anggotaB)
print("hasil irisan :")
print(irisan)

#operasi selisih
selisih = anggotaA.difference(anggotaB)
print ("Hasil Selisih himpunan A - himpunan B :")
print(selisih)