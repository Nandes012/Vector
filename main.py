from feature.tambah import tambah
from feature.kurang import kurang
def main():
    while True:
        print("\nOperasi pada vektor 2D")
        print("1. Penjumlahan vektor")
        print("2. Pengurangan vektor")
        print("3. Dot Product")
        print("4. Panjang Vektor")
        print("5. Vektor Unit")
        print("6. Keluar")

        pilihan = input("Masukkan nomor 1-6: ")

        if pilihan == "6":
            print("Program selesai.")
            break

        try:
            vektor_a = list(map(int, input("Masukkan vektor A (dalam format x,y): ").split(',')))
            vektor_b = list(map(int, input("Masukkan vektor B (dalam format x,y): ").split(',')))
        except ValueError:
            print("Input tidak valid, silakan masukkan vektor dalam format x,y.")
            continue

        if pilihan == "1": 
            hasil = tambah(vektor_a, vektor_b)
            print("Hasil Penjumlahan:", hasil)
        elif pilihan == "2":
            print("Hasil Pengurangan:", kurang(vektor_a, vektor_b))
        elif pilihan == "3":
            print("Hasil Dot Product:", dot_product(vektor_a, vektor_b))
        elif pilihan == "4":
            print("Panjang Vektor A:", panjang(vektor_a))
            print("Panjang Vektor B:", panjang(vektor_b))
        elif pilihan == "5":
            print("Vektor Unit A:", unit_vector(vektor_a))
            print("Vektor Unit B:", unit_vector(vektor_b))
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
 main()