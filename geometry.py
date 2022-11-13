import lingkaran
import persegipanjang

PILIHAN_LUAS_LINGKARAN = 1
PILIHAN_KELILING_LINGKARAN = 2
PILIHAN_LUAS_PERSEGIPANJANG = 3
PILIHAN_KELILING_PERSEGIPANJANG = 4
PILIHAN_KELUAR = 5

def tampilan_menu():
    print('menu')
    print('1) Luas Lingkaran')
    print('2) Keliling Lingkaran')
    print('3) Luas Persegi Panjang')
    print('4) Keliling Persegi Panjang')
    print('5) Keluar')

def main():
    pilihan = 0

    while pilihan != PILIHAN_KELUAR:
        tampilan_menu()
        pilihan = int(input('masukan pilihan anda :'))
        if pilihan == PILIHAN_LUAS_LINGKARAN:
            radius = float(input('masukan radius lingkaran:'))
            print('Luas Lingkaran Adalah :', lingkaran.luas(radius))
        elif pilihan == PILIHAN_KELILING_LINGKARAN:
            radius = float(input('masukan radius lingkaran'))
            print('keliling lingkaran adalah', lingkaran.keliling(radius))
        elif pilihan == PILIHAN_LUAS_PERSEGIPANJANG:
            lebar = float (input('masukan lebar persegi panjang :'))
            panjang = float(input('masukan panjang persegi panjang :'))
            print('luas persegi panjang adalah :', persegipanjang.luas(lebar,panjang))
        elif pilihan == PILIHAN_KELILING_PERSEGIPANJANG:
            lebar = float (input('masukan lebar persegi panjang :'))
            panjang = float(input('masukan panjang persegi panjang :'))
            print('keliling persegi panjang adalah :', persegipanjang.keliling(lebar,panjang))
        elif pilihan == PILIHAN_KELUAR:
            print('keluar dari program')
        else:
            print('error: pilihan tidak valid')

main()
