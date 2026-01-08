from utils import bersihkan_layar, konversi_nilai_ke_label, hitung_ips

def main():
    daftar_sks = []
    daftar_bobot = []
    konversi_huruf = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

    while True:
        print("\n========================")
        print("    PROGRAM NILAI CLI   ")
        print("========================")
        print("1. Konversi Nilai ke Label")
        print("2. Konversi Label ke Bobot")
        print("3. Tambah Data Mata Kuliah")
        print("4. Lihat Total & IPS")
        print("5. Bersihkan Layar")
        print("6. Exit")
        
        pilihan = input("\nPilihan: ")

        if pilihan == '1':
            try:
                n = float(input("Masukkan nilai angka (0-100): "))
                print(f"Label Nilai: {konversi_nilai_ke_label(n)}")
            except ValueError:
                print("Input harus angka!")

        elif pilihan == '2':
            label = input("Label Nilai (A-E): ").upper()
            print(f"Bobot: {konversi_huruf.get(label, 'Tidak Valid')}")

        elif pilihan == '3':
            try:
                sks = int(input("Masukkan SKS: "))
                huruf = input("Masukkan Label (A-E): ").upper()
                if huruf in konversi_huruf:
                    daftar_sks.append(sks)
                    daftar_bobot.append(konversi_huruf[huruf])
                    print("Data tersimpan!")
                else:
                    print("Label salah!")
            except ValueError:
                print("SKS harus angka!")

        elif pilihan == '4':
            ips, t_sks, t_poin = hitung_ips(daftar_sks, daftar_bobot)
            print(f"\n--- Ringkasan ---")
            print(f"Total SKS   : {t_sks}")
            print(f"Total Poin  : {t_poin}")
            print(f"IPS         : {ips:.2f}")

        elif pilihan == '5':
            bersihkan_layar()

        elif pilihan == '6':
            print("Sampai Jumpa!")
            break

if __name__ == "__main__":
    main()