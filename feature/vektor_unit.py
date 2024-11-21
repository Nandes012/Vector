from feature.panjang import panjang
def unit_vector(vektor):
    magnitude = panjang(vektor)
    if magnitude == 0:
        raise ValueError("Vektor nol tidak memiliki vektor unit.")
    return [comp / magnitude for comp in vektor]