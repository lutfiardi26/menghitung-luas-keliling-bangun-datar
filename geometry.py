import lingkaran
import persegipanjang
import segitiga

def tampilan_menu():
    print('menu')
    print('1) Luas Lingkaran')
    print('2) Keliling Lingkaran')
    print('3) Luas Persegi Panjang')
    print('4) Keliling Persegi Panjang')
    print('5) Luas Segitiga')
    print('6) Keliling Segitiga')
    print('7) Keluar')

def main():
    pilihan = 0

    while pilihan != 7:
        tampilan_menu()
        pilihan = int(input('masukan pilihan anda :'))
        if pilihan == 1:
            radius = float(input('masukan radius lingkaran:'))
            print('Luas Lingkaran Adalah :', lingkaran.luas(radius))
        elif pilihan == 2:
            radius = float(input('masukan radius lingkaran'))
            print('keliling lingkaran adalah', lingkaran.keliling(radius))
        elif pilihan == 3:
            lebar = float (input('masukan lebar persegi panjang :'))
            panjang = float(input('masukan panjang persegi panjang :'))
            print('luas persegi panjang adalah :', persegipanjang.luas(lebar,panjang))
        elif pilihan == 4:
            lebar = float (input('masukan lebar persegi panjang :'))
            panjang = float(input('masukan panjang persegi panjang :'))
            print('keliling persegi panjang adalah :', persegipanjang.keliling(lebar,panjang))
        elif pilihan == 5:
            alas = float (input('masukan alas segitiga :'))
            tinggi = float (input('masukan tinggi segitiga :'))
            print('luas segitiga adalah :', segitiga.luas(alas,tinggi))
        elif pilihan == 6:
            sisi = float (input('masukan panjang sisi segitiga :'))
            print('Keliling Segitiga adalah :', segitiga.keliling(sisi))
        elif pilihan == 7:
            print('keluar dari program')
        else:
            print('error: pilihan tidak valid')

main()
