import math

def tambah(vektor_a, vektor_b):
    if len(vektor_a) != len(vektor_b):
        raise ValueError("Panjang vektor harus sama untuk penjumlahan.")
    return [vektor_a[i] + vektor_b[i] for i in range(len(vektor_a))]