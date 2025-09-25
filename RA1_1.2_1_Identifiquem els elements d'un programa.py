import math

PI = 3,1416 #constant

def clacular_area(radi): #variable
    return PI * radi ** 2 #funció

radi = float(input("introdueix el radi: ")) #linia del usuari
area = calcular_area(radi) 
print("L'àrea del cercle és:", area) #linia resultat
