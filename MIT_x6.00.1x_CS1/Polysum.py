import math

def polysum(n, s):
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    perimeter_sq = (n * s)**2
    return round(area + perimeter_sq, 4)
