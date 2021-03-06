from tabulate import tabulate
import csv
import os
import pandas as pd

csv_filename_akun = "akun.csv"
csv_filename_inventori = "data_sepatu.csv"
csv_filename_output = "output.csv"

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
    if not os.path.exists(csv_filename_output):
        with open(csv_filename_output, mode="w") as csv_file:
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
    with open(csv_filename_akun, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = []
    indeks = 0
    for data in akun:
        if data["Username"] == username and data["Password"] == password:
            data_found = akun[indeks]
            break
        indeks += 1
    if len(data_found) > 0:
        print("\n\t\t\t\t\t<<<< Login berhasil >>>>")
        data_found.clear()
        balik_ke_menu_awal()    
    else:
        print("\n<<<< USERNAME ATAU PASSWORD SALAH >>>>")
        data_found.clear()
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
    menu_pilihan = input("Masukkan Pilihan > ")
    if menu_pilihan == "1":
        tampil_data()
        pilih_sorting()
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

def tampil_data():
    clear_screen()
    print("")
    try:
        f = pd.read_csv(csv_filename_inventori, sep=',') 
        print(tabulate(f, headers= f, tablefmt='fancy_outline', stralign='left', numalign='center', showindex=False))
    except:
        print("<<<< DATA KOSONG >>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        menu_awal()

##########################################################################################################################################################################################
##########################################################################################################################################################################################

def pilih_sorting():
    tampil_data()
    print("===========================================================================")
    print("|                              MENU SORTING                               |")
    print("===========================================================================")
    print("|                                                                         |")
    print("| Silahkan Pilih Sorting Kode Data Secara :                               |")
    print("| [1] Ascending                                                           |")
    print("| [2] Descending                                                          |")    
    print("| [0] Kembali                                                             |")    
    print("|                                                                         |")
    print("===========================================================================")
    pilih = input("Masukkan Pilihan > ")
    if pilih == "1":
        cara = "Ascending"
        pilih_asce_desc(cara)
        balik_ke_menu_awal()
    elif pilih == "2":
        cara = "Descending"
        pilih_asce_desc(cara)
        balik_ke_menu_awal()
    elif pilih == "0":
        balik_ke_menu_awal()
    else:
        print("<<<<< INVALID INPUT >>>>>")
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        menu_awal()

def pilih_asce_desc(cara):
    clear_screen()
    if cara == "Ascending":
            tampil_data()
            print("===========================================================================")
            print("|                         ASCENDING KODE BARANG                           |")
            print("===========================================================================")
            print("|                                                                         |")
            print("| Silahkan Pilih Metode Sort :                                            |")
            print("| [1] Bubble Sort                                                         |")
            print("| [2] Insertion Sort                                                      |")
            print("| [3] Selection Sort                                                      |")
            print("| [4] Quick Sort                                                          |")
            print("| [5] Merge Sort                                                          |")
            print("| [6] Shell Sort                                                          |")
            print("| [0] Kembali                                                             |")
            print("|                                                                         |")
            print("===========================================================================")
            pilih_metode = input("Masukkan Pilihan > ")
            if pilih_metode == "1":
                clear_screen()
                print("===========================================================================")
                print("|                             BUBBLE SORT                                 |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Bubble Sort                           |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                bubbleSort(reskodeStr, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "2":
                clear_screen()
                print("===========================================================================")
                print("|                            INSERTION SORT                               |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Insertion Sort                        |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                insertionSort(reskodeStr, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "3":
                clear_screen()
                print("===========================================================================")
                print("|                            SELECTION SORT                               |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Selection Sort                        |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                selectionSort(reskodeStr, len(reskodeStr), method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "4":
                clear_screen()
                print("===========================================================================")
                print("|                               QUICK SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Quick Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                quickSort(reskodeStr, 0, len(reskodeStr)-1, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "5":
                clear_screen()
                print("===========================================================================")
                print("|                               MERGE SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Merge Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                mergeSort(reskodeStr, 0, len(reskodeStr)-1, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "6":
                clear_screen()
                print("===========================================================================")
                print("|                               SHELL SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Shell Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               ASCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Ascending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                shellSort(reskodeStr, len(reskodeStr), method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "0":
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                pilih_sorting()
            else:
                print("<<<< INVALID INPUT >>>>")
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                pilih_asce_desc("Ascending")
    elif cara == "Descending": 
            tampil_data()
            print("===========================================================================")
            print("|                         DESCENDING KODE BARANG                          |")
            print("===========================================================================")
            print("|                                                                         |")
            print("| Silahkan Pilih Metode Sort :                                            |")
            print("| [1] Bubble Sort                                                         |")
            print("| [2] Insertion Sort                                                      |")
            print("| [3] Selection Sort                                                      |")
            print("| [4] Quick Sort                                                          |")
            print("| [5] Merge Sort                                                          |")
            print("| [6] Shell Sort                                                          |")
            print("| [0] Kembali                                                             |")
            print("|                                                                         |")
            print("===========================================================================")
            pilih_metode = input("Masukkan Pilihan > ")
            if pilih_metode == "1":
                clear_screen()
                print("===========================================================================")
                print("|                             BUBBLE SORT                                 |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Bubble Sort                           |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                              DESCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                bubbleSort(reskodeStr, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "2":
                clear_screen()
                print("===========================================================================")
                print("|                            INSERTION SORT                               |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Insertion Sort                        |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                              DESCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                insertionSort(reskodeStr, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "3":
                clear_screen()
                print("===========================================================================")
                print("|                            SELECTION SORT                               |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Selection Sort                        |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                              DESCENDING                                 |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                selectionSort(reskodeStr, len(reskodeStr), method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "4":
                clear_screen()
                print("===========================================================================")
                print("|                               QUICK SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Quick Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               DESCENDING                                |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                quickSort(reskodeStr, 0, len(reskodeStr)-1, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "5":
                clear_screen()
                print("===========================================================================")
                print("|                               MERGE SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Merge Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               DESCENDING                                |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                mergeSort(reskodeStr, 0, len(reskodeStr)-1, method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "6":
                clear_screen()
                print("===========================================================================")
                print("|                               SHELL SORT                                |")
                print("===========================================================================")
                print("|                                                                         |")
                print("| Data Di Sortir Menggunakan Metode Shell Sort                            |")
                print("|                                                                         |")
                print("===========================================================================")
                print("|                               DESCENDING                                |")
                print("===========================================================================")
                reskodeStr = []
                resdict = []
                newdict = []
                method = "Descending"
                with open(csv_filename_inventori, mode='r') as csv_file: 
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        reskodeStr.append(row["Kode"])
                        resdict.append(row)
                shellSort(reskodeStr, len(reskodeStr), method)
                indeks = 0
                for u in resdict:
                    searchKode(resdict, reskodeStr[indeks], newdict)
                    indeks += 1
                with open(csv_filename_output, mode='w') as sortedList:
                    fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                    writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                    writer.writeheader()
                    for new_data in newdict:
                        writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
                sdf = pd.read_csv(csv_filename_output, sep=',')
                print("")
                print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='left', showindex=False))
            elif pilih_metode == "0":
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                pilih_sorting()
            else:
                print("<<<< INVALID INPUT >>>>")
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                pilih_asce_desc("Descending")

def searchKode(arr, kode, newarr):
    for k in arr:
        if k["Kode"] == kode:
            newarr.append(k)
    return newarr

def bubbleSort(array, method):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if method == "Ascending":
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            if method == "Descending":
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array

def insertionSort(array, method):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        if method == "Ascending":
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        if method == "Descending":
            while j >= 0 and key > array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key

def selectionSort(array, size, method):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if method == "Ascending":
                if array[i] < array[min_idx]:
                    min_idx = i
            if method == "Descending":
                if array[i] > array[min_idx]:
                    min_idx = i
        array[step], array[min_idx] = array[min_idx],array[step]

def partition(array, low, high, order):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if order == "Ascending":
            if array[j] <= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
        elif order == "Descending":
            if array[j] >= pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high, order):
    if low < high:
        pi = partition(array, low, high, order)
        quickSort(array, low, pi - 1, order)
        quickSort(array, pi + 1, high, order)

def merge(arr, l, m, r, order):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 :
        if order == "Ascending":
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        elif order == "Descending":
            if L[i] >= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r, order):
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(arr, l, m, order)
        mergeSort(arr, m + 1, r, order)
        merge(arr, l, m, r, order)

def shellSort(array, n, order):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            if order == "Ascending":
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
            elif order == "Descending":
                while j >= interval and array[j - interval] < temp:
                    array[j] = array[j - interval]
                    j -= interval
            array[j] = temp
        interval //= 2

##########################################################################################################################################################################################
##########################################################################################################################################################################################

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
        menu_awal()
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
                tanyakan = input("Apakah Anda Yakin? \n[1] Ya\n[2] Tidak\nMasukkan Pilihan > ")
                if tanyakan == "1":
                    writer.writerow({'Kode': kode, 'Nama': nama, 'Merk': merk, 'Ukuran': ukuran, 'Warna': warna, 'Harga': harga, 'Jumlah': jumlah})
                    print("\nKode             : ", kode)
                    print("Nama Barang      : ", nama)
                    print("Merk Sepatu      : ", merk)
                    print("Ukuran Sepatu    : ", ukuran)
                    print("Warna            : ", warna)
                    print("Harga            : ", harga)
                    print("Jumlah           : ", jumlah)
                    input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                elif tanyakan == "2":
                    input("\n[ Tekan ENTER untuk melanjutkan.... ]")           
            except ValueError:
                print("\n<<<< INVALID INPUT >>>>")
                input("\n[ Tekan ENTER untuk melanjutkan.... ]")
                menu_awal()
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
        reader = csv.DictReader(csv_file)
        for row in reader:
            data_sementara.append(row)
            for j in data_sementara:
                if j["Kode"] == kodebarang:
                    data_sementara.remove(j)
    yakin = str(input("Apakah Anda Yakin? y/t > "))
    if yakin == 'y':
        with open(csv_filename_inventori, 'w') as writeFile: # Belum
            fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
            writer = csv.DictWriter(writeFile, fieldnames= fieldnames)
            writer.writeheader()
            for new_data in data_sementara:
                writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
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

def cari_data():
    clear_screen()
    print("===========================================================================")
    print("|                                MENU CARI                                |")
    print("===========================================================================")
    print("|                                                                         |")
    print("| Silahkan Pilih Yang Ingin Di Cari :                                     |")
    print("| [1] Nama Barang                                                         |")
    print("| [2] Merk Sepatu                                                         |")
    print("| [0] Kembali                                                             |")
    print("|                                                                         |")
    print("===========================================================================")
    pilih_cari = input("Masukkan Pilihan > ")
    if pilih_cari == "1":
        resdict = []
        newdict = []
        with open(csv_filename_inventori, mode='r') as csv_file: 
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                resdict.append(row)
        dicari = str(input("Masukkan Nama Yang Ingin Di Cari : "))
        linearSearch(resdict, dicari, newdict, "nama")
        with open(csv_filename_output, mode='w') as sortedList:
                fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in newdict:
                    writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
        sdf = pd.read_csv(csv_filename_output, sep=',')
        print("")
        print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='center', showindex=False))
        if len(newdict) < 1:
            print("<<<<< NAMA TIDAK ADA >>>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            cari_data()
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        cari_data()
    elif pilih_cari == "2":
        resdict = []
        newdict = []
        with open(csv_filename_inventori, mode='r') as csv_file: 
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for row in csv_reader:
                resdict.append(row)
        dicari = str(input("Masukkan Merk Yang Ingin Di Cari : "))
        linearSearch(resdict, dicari, newdict, "merk")
        with open(csv_filename_output, mode='w') as sortedList:
                fieldnames = ['Kode', 'Nama', 'Merk', 'Ukuran', 'Warna', 'Harga', 'Jumlah']
                writer = csv.DictWriter(sortedList, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in newdict:
                    writer.writerow({'Kode': new_data['Kode'], 'Nama': new_data['Nama'], 'Merk': new_data['Merk'], 'Ukuran': new_data['Ukuran'], 'Warna': new_data['Warna'], 'Harga': new_data['Harga'], 'Jumlah': new_data['Jumlah']})
        sdf = pd.read_csv(csv_filename_output, sep=',')
        print("")
        print(tabulate(sdf, headers= sdf, tablefmt='fancy_outline', stralign='left', numalign='center', showindex=False))
        if len(newdict) < 1:
            print("<<<<< MERK TIDAK ADA >>>>>")
            input("\n[ Tekan ENTER untuk melanjutkan.... ]")
            cari_data()
        input("\n[ Tekan ENTER untuk melanjutkan.... ]")
        cari_data()
    elif pilih_cari == "0":
        balik_ke_menu_awal()

def linearSearch(arr, dicari, newarr, mencari):
    for k in arr:
        if mencari == "nama":
            if k["Nama"] == dicari:
                newarr.append(k) 
        elif mencari == "merk":
            if k["Merk"] == dicari:
                newarr.append(k)
    print("\n<<<< Data Ditemukan >>>>")
    return newarr

check_database()
login()
