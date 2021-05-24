import pynput
from tabulate import tabulate
import csv
import os
import pandas as pd

csv_filename_akun = "akun.csv"
csv_filename_inventori = "data_sepatu.csv"

def check_database():
    if not os.path.exists(csv_filename_akun):
        with open(csv_filename_akun, mode='w') as csv_file:
            fieldnames = ["Username", "Password"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerow({"Username": "admin", "Password": 1234})
    if not os.path.exists(csv_filename_inventori):
        with open(csv_filename_inventori, mode='w') as csv_file:
            fieldnames = ["Kode", "Nama", "Merk", "Ukuran", "Warna", "Harga", "Jumlah"]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def login():
    clear_screen()
    print("===========================================================================================================")
    print("|  /$$$$$$$$        /$$                        /$$$$$$                                  /$$               |")
    print("| |__  $$__/       | $$                       /$$__  $$                                | $$               |")
    print("|    | $$  /$$$$$$ | $$   /$$  /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$   /$$ |")
    print("|    | $$ /$$__  $$| $$  /$$/ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$ |____  $$|_  $$_/  | $$  | $$ |")
    print("|    | $$| $$  \ $$| $$$$$$/ | $$  \ $$       \____  $$| $$$$$$$$| $$  \ $$  /$$$$$$$  | $$    | $$  | $$ |")
    print("|    | $$| $$  | $$| $$_  $$ | $$  | $$       /$$  \ $$| $$_____/| $$  | $$ /$$__  $$  | $$ /$$| $$  | $$ |")
    print("|    | $$|  $$$$$$/| $$ \  $$|  $$$$$$/      |  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/ |")
    print("|    |__/ \______/ |__/  \__/ \______/        \______/  \_______/| $$____/  \_______/   \___/   \______/  |")
    print("|                                                                | $$                                     |")
    print("|                                                                | $$                                     |")
    print("|                                                                |__/                                     |")
    print("===========================================================================================================")
    print("|                                               [ LOGIN ]                                                 |")
    print("===========================================================================================================")
    print("                                            [ MASUKKAN AKUN ]                                              ")
    username = input("\t\t\t\t\tUsername : ")
    password = input("\t\t\t\t\tPassword : ")
    akun = []
    data_found = []
    indeks = 0
    with open(csv_filename_akun, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    for data in akun:
        if data["Username"] == username:
            data_found = akun[indeks]
        indeks += 1
    if len(data_found) > 0:
        if data_found["Password"] == password:
            print("\n\t\t\t\t\t<<<< Login berhasil >>>>")
            balik_ke_menu_awal()
    else:
        print("\n<<<< USERNAME ATAU PASSWORD SALAH >>>>")
        balik_ke_login()

def balik_ke_login():
    input("\n[ Tekan ENTER untuk melanjutkan.... ]")
    login()

def balik_ke_menu_awal():
    input("\n[ Tekan ENTER untuk melanjutkan.... ]")
    menu_awal()


def menu_awal():
    clear_screen()
    print("===========================================================================================================")
    print("|  /$$$$$$$$        /$$                        /$$$$$$                                  /$$               |")
    print("| |__  $$__/       | $$                       /$$__  $$                                | $$               |")
    print("|    | $$  /$$$$$$ | $$   /$$  /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$   /$$   /$$ |")
    print("|    | $$ /$$__  $$| $$  /$$/ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$ |____  $$|_  $$_/  | $$  | $$ |")
    print("|    | $$| $$  \ $$| $$$$$$/ | $$  \ $$       \____  $$| $$$$$$$$| $$  \ $$  /$$$$$$$  | $$    | $$  | $$ |")
    print("|    | $$| $$  | $$| $$_  $$ | $$  | $$       /$$  \ $$| $$_____/| $$  | $$ /$$__  $$  | $$ /$$| $$  | $$ |")
    print("|    | $$|  $$$$$$/| $$ \  $$|  $$$$$$/      |  $$$$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$/ |")
    print("|    |__/ \______/ |__/  \__/ \______/        \______/  \_______/| $$____/  \_______/   \___/   \______/  |")
    print("|                                                                | $$                                     |")
    print("|                                                                | $$                                     |")
    print("|                                                                |__/                                     |")
    print("===========================================================================================================")
    print("|                                          ADMIN TOKO SEPATU                                              |")
    print("===========================================================================================================")
    print("|                                                                                                         |")
    print("| Silahkan Pilih :                                                                                        |")
    print("| [1] Tampilkan Data                                                                                      |")
    print("| [2] Tambahkan Data                                                                                      |")
    print("| [3] Hapus Data                                                                                          |")
    print("| [4] Edit Data                                                                                           |")
    print("| [5] Cari Data                                                                                           |")
    print("| [0] Exit                                                                                                |")
    print("|                                                                                                         |")
    print("===========================================================================================================")
    menu_pilihan = input("Masukkan Pilihan> ")
    if menu_pilihan == "1":
        tampil_data()
    elif menu_pilihan == "2":
        tambah_data()
    elif menu_pilihan == "3":
        hapus_data()
    elif menu_pilihan == "4":
        edit_data()
    elif menu_pilihan == "5":
        cari_data()
    elif menu_pilihan == "0":
        clear_screen()
        exit()
    else:
        print("<<<<< INVALID INPUT >>>>>")
        balik_ke_menu_awal()

def tampil_data(): # Masukkan Pilihan Sorting data secara Ascending dan Descending ( Belum Ini )
    clear_screen()
    print("")
    try:
        f = pd.read_csv(csv_filename_inventori, sep=',') 
        print(tabulate(f, headers= f, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
        print("===========================================================================")
        print("|                                MENU SORTING                             |")
        print("===========================================================================")
        print("|                                                                         |")
        print("| Silahkan Pilih Sorting Data Secara :                                    |")
        print("| [1] Ascending                                                           |")
        print("| [2] Decending                                                           |")
        print("|                                                                         |")
        print("===========================================================================")
        pilih = input("Masukkan Pilihan > ")
        if pilih == "1":
            cara = "Ascending"
            sorting(cara)
            balik_ke_menu_awal()
        elif pilih == "2":
            cara = "Decending"
            sorting(cara)
            balik_ke_menu_awal()
        else:
            print("<<<<< INVALID INPUT >>>>>")
            balik_ke_menu_awal()
    except:
        print("<<<< DATA KOSONG >>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        menu_awal()

def sorting(cara):
    if cara == "Ascending":
        print("Ascending")
    elif cara == "Decending":
        print("Descending")

def tambah_data():
    tampil_data()
    print("===========================================================================")
    print("|                               MENU TAMBAH                               |")
    print("===========================================================================")
    print("|                                                                         |")
    print("| Silahkan Masukkan Data Berikut:                                         |")
    print("| <> Kode Barang                                                          |")
    print("| <> Nama Barang                                                          |")
    print("| <> Merk Barang                                                          |")
    print("| <> Ukuran Barang                                                        |")
    print("| <> Warna Barang                                                         |")
    print("| <> Harga Barang                                                         |")
    print("| <> Jumlah Barang                                                        |")
    print("|                                                                         |")
    print("===========================================================================")
    data_sementara = []
    data_found = []
    with open(csv_filename_inventori, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_sementara.append(row)
    kode = input("\nMasukkan Kode Barang > ")
    if kode == "":
        print("\n<<<< INVALID KODE >>>> ")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        data_sementara.clear()
        tambah_data()
    indeks = 0
    for data in data_sementara:
        if(data['Kode'] == kode):
            data_found = data_sementara[indeks]
        indeks += 1
    if len(data_found) > 0:
        print("<<<< KODE SUDAH ADA >>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        data_found.clear()
        data_sementara.clear()
        tambah_data()
    else:
        with open(csv_filename_inventori, 'a') as csv_file:
            fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            try:
                nama = str(input("Masukkan Nama Barang > "))
                merk = str(input("Masukkan Merk Sepatu > "))
                ukuran = int(input("Masukkan Ukuran Sepatu > "))
                warna = str(input("Masukkan Warna Sepatu > "))
                harga = int(input("Masukkan Harga > "))
                jumlah = int(input("Masukkan Jumlah > "))
                writer.writerow({'Kode': kode, 'Nama': nama, 'Merk': merk, 'Ukuran': ukuran, 'Warna': warna, 'Harga': harga, 'Jumlah': jumlah})
            except ValueError:
                print("\n<<<< INVALID INPUT >>>>")
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                tambah_data()
        print("\nKode             : "+ kode)
        print("Nama Barang      : "+ nama)
        print("Merk Sepatu      : "+ merk)
        print("Ukuran Sepatu    : "+ ukuran)
        print("Warna            : "+ warna)
        print("Harga            : "+ harga)
        print("Jumlah           : "+ jumlah)
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        data_found.clear()
        data_sementara.clear()
        menu_awal()

def hapus_data():
    clear_screen()
    tampil_data()
    print("===========================================================================")
    print("|                               MENU HAPUS                                |")
    print("===========================================================================")
    print("|                                                                         |")
    print("| Silahkan Masukkan Kode Barang Yang Ingin Di Hapus :                     |")
    print("|                                                                         |")
    print("|                                                                         |")
    print("===========================================================================")
    data_sementara = []
    kodebarang = input("Masukkan Kode Barang > ")
    with open(csv_filename_inventori, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data_sementara.append(row)
            for field in row:
                if field == kodebarang:
                    data_sementara.remove(row)
    yakin = str(input("Apakah Anda Yakin? y/t > "))
    if yakin == 'y':
        with open(csv_filename_inventori, 'w') as writeFile:
            writer = csv.writer(writeFile, lineterminator='\n')
            writer.writerows(data_sementara)
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        data_sementara.clear()
        menu_awal()
    elif yakin == 't':
        balik_ke_menu_awal()
        data_sementara.clear()
    else:
        print("<<<< INVALID INPUT >>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        hapus_data()

def edit_data():
    tampil_data()
    print("===========================================================================")
    print("|                                MENU EDIT                                |")
    print("===========================================================================")
    print("|                                                                         |")
    print("| Silahkan Pilih Yang Ingin Di Edit :                                     |")
    print("| [1] Nama Barang                                                         |")
    print("| [2] Merk Sepatu                                                         |")
    print("| [3] Warna Sepatu                                                        |")
    print("| [4] Harga Barang                                                        |")
    print("| [5] Jumlah Barang                                                       |")
    print("| [6] Ukuran Sepatu                                                       |")
    print("| [0] Kembali                                                             |")
    print("|                                                                         |")
    print("===========================================================================")
    data_edit = []
    data_found = []
    pilihan = input("Masukkan Pilihan > ")
    tampil_data()
    with open(csv_filename_inventori) as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for row in csv_reader:
            data_edit.append(row)
    if pilihan == "1":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            nama_baru = str(input("Masukkan Nama Baru > "))
            indeks = 0
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Nama'] = nama_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    if pilihan == "2":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            indeks = 0
            merk_baru = str(input("Masukkan Merk Baru > "))
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Merk'] = merk_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    if pilihan == "3":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            warna_baru = str(input("Masukkan Warna Baru > "))
            indeks = 0
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Warna'] = warna_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    if pilihan == "4":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            harga_baru = int(input("Masukkan Harga Baru > "))
            indeks = 0
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Harga'] = harga_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    if pilihan == "5":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            jumlah_baru = int(input("Masukkan Jumlah Baru > "))
            indeks = 0
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Jumlah'] = jumlah_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    if pilihan == "6":
        try:
            kode_barang = input("Masukkan Kode Barang Yang Ingin Di Edit : ")
            ukuran_baru = int(input("Masukkan Ukuran Baru > "))
            indeks = 0
            for data in data_edit:
                if (data['Kode'] == kode_barang):
                    data_edit[indeks]['Ukuran'] = ukuran_baru
                    data_found = data_edit[indeks]
                indeks += 1
            if len(data_found) > 0:
                with open(csv_filename_inventori, mode='w') as csv_file:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in data_edit:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                tampil_data()
                data_edit.clear()
                data_found.clear()
                balik_ke_menu_awal()
            else:
                print("<<<< DATA TIDAK ADA >>>>")
                data_edit.clear()
                data_found.clear()
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                edit_data()
        except ValueError:
            print("<<<< INVALID INPUT >>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            data_edit.clear()
            data_found.clear()
            edit_data()
    elif pilihan == "0":
        menu_awal()
    else:
        print("<<<< INVALID INPUT >>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        edit_data()

login()


