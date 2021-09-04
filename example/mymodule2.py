import math
import area

def calcDelta(a,b,c):        
    delta = (b*b) - (4 * a * c) 
    print(delta)

def calcRaiz(a,b,delta):        
    raiz1 = (-b - math.sqrt(delta))/(2*a) 
    raiz2 = (-b + math.sqrt(delta))/(2*a) 
    print('Raiz 1', raiz1)
    print('Raiz 2', raiz2)

a = 1
b = 2
c = -2

calcDelta(a,b,c)

a = 1
b = 2
c = -1

calcDelta(a,b,c)


