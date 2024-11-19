import math

def panjang(vektor):
    if len(vektor) != 2:
        raise ValueError("Vektor harus memiliki dua komponen (x dan y).")
    x, y = vektor
    return math.sqrt(x*2+y*2)