import os

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bobot(n):
    # Menggunakan logika perbandingan yang lebih ringkas
    for limit, bbt in [(80, 4), (75, 3.5), (70, 3), (65, 2.5), (60, 2), (50, 1)]:
        if n >= limit: return bbt
    return 0

def input_data(jumlah):
    sks = [int(input(f"SKS {i+1}: ")) for i in range(jumlah)]
    print("\n---------- input Nilai Mahasiswa ----------")
    bobot = [get_bobot(float(input(f"Nilai {i+1}: "))) for i in range(jumlah)]
    return sks, bobot

def main():
    daftar_sks, daftar_bobot = [], []
    konversi_huruf = {'A': 4, 'B+': 3.5, 'B': 3, 'C+': 2.5, 'C': 2, 'D': 1, 'E': 0}

    while True:
        bersihkan_layar()
        print("---------- menu ----------\n1. Konversi Nilai ke Label\n2. Konversi Label ke Bobot\n3. Total SKS\n4. Total Nilai\n5. Hitung IPS\n6. Exit")
        pilih = input("\nPilihan: ")

        try:
            if pilih == '1':
                n = float(input("Nilai Mahasiswa: "))
                # Mencari label berdasarkan bobot
                b = get_bobot(n)
                label = [k for k, v in konversi_huruf.items() if v == b][0]
                print(f"Label Nilai: {label}")

            elif pilih == '2':
                label = input("Label Nilai Mahasiswa: ").upper()
                print(f"Bobot: {konversi_huruf.get(label, 'Tidak valid')}")

            elif pilih in ['3', '4', '5']:
                if not daftar_sks or pilih == '3': # Input ulang jika menu 3 atau data kosong
                    jml = int(input("Jumlah Data: "))
                    if pilih == '3':
                        daftar_sks = [int(input(f"SKS {i+1}: ")) for i in range(jml)]
                    else:
                        daftar_sks, daftar_bobot = input_data(jml)

                t_sks = sum(daftar_sks)
                t_nilai = sum(s * b for s, b in zip(daftar_sks, daftar_bobot))

                if pilih == '3': print(f"Total SKS: {t_sks}")
                elif pilih == '4': print(f"Total Nilai: {t_nilai}")
                elif pilih == '5': print(f"IPS: {t_nilai/t_sks:.1f}")

            elif pilih == '6': break
        except Exception as e:
            print(f"Error: {e}")
        
        input("\nTekan Enter...")

if __name__ == "__main__":
    main()