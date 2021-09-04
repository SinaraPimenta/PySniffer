import math

def esfera(r):
    area = (4/3) * math.pi * r * r * r
    print(area)
    return area

def paralelepipedo(b,h,l):
    area = b * h * l
    print(area)
    return area

def piramide(areabase,h):
    area = (areabase * h) / 3
    print(area)
    return area

def cubo(l):
    area = (l * l * l) 
    print(area)
    return area
