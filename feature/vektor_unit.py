import numpy as np

def unit_vector(v):
    magnitude = np.linalg.norm(v)  # Panjang vektor
    if magnitude == 0:
        raise ValueError("Vektor nol tidak memiliki vektor satuan.")
    return v / magnitude
