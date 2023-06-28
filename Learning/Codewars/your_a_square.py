from math import sqrt

def is_square(n):
    if n >= 0:
        sr = int(sqrt(n))
        return (sr * sr) == n
    return False

