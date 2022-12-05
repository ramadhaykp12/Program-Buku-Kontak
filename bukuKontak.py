import os
def daftarKontak():  # fungsi untuk menampilkan kontak yang tersimpan di list kontak
    file_exists = os.path.exists('myfile.txt')
    if file_exists == True:
      file_path1 = open('myfile.txt','r')
      while True:
         line = file_path1.readline()
         if not line:
           break
         print(line.replace("[","").replace("]",""))
    else:
      print('Belum Ada Data')
      print('Silahkan masukkan data terlebih dahulu')

def tambahKontak():  # fungsi untuk menambahkan kontak
    namaKontak = []
    noTelepon = []
    alamat = []
    emailPribadi = []
    nama= input('Nama: ')
    namaKontak.append(nama)
    no=input('No Telepon: ')
    noTelepon.append(no)
    address=input('Alamat: ')
    alamat.append(address)
    email=input('Email: ')
    emailPribadi.append(email)
    print('Kontak berhasil ditambahkan')
    namaKontak = str(namaKontak)
    noTelepon = str(noTelepon)
    alamat = str(alamat)
    emailPribadi = str(emailPribadi)
    file1 = open('myfile.txt','a')
    file1.write('---------------------')
    file1.write('\n')
    file1.write('Nama :' + namaKontak)
    file1.write('\n')
    file1.write('Nomor Telepon:' + noTelepon)
    file1.write('\n')
    file1.write('Alamat :' + alamat)
    file1.write('\n')
    file1.write('Email :' + emailPribadi)
    file1.write('\n') 
    file1.write('---------------------')
    file1.close()

def HapusKontak():
    os.remove('myfile.txt')


print('Selamat datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Hapus Kontak')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        daftarKontak()
    elif menu == 2:
        tambahKontak()
    elif menu == 3:
        HapusKontak()
    elif menu == 4:
        break
    else:
        print('Menu tidak tersedia')
