# a. Una constant
FACTOR_CONVERSIO = 100  # Per convertir m² a cm²

# b. Una funció
def calcular_area(base, altura):
    return base * altura

# c. Una entrada de l'usuari
print("Calculadora d'àrea d'un rectangle")
base = float(input("Introdueix la base del rectangle (en metres): "))
altura = float(input("Introdueix l'altura del rectangle (en metres): "))

# Càlcul utilitzant la funció
area_metres = calcular_area(base, altura)
area_centimetres = area_metres * FACTOR_CONVERSIO

# d. Una sortida per pantalla
print("\n" + "="*40)
print(f"Base: {base} m")
print(f"Altura: {altura} m")
print(f"Àrea: {area_metres} m²")
print(f"Àrea en centímetres quadrats: {area_centimetres} cm²")
print("="*40)