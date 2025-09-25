print("=== CALCULADORA BÀSICA ===")

# Demanar dos números
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

print("\nSelecciona una operació:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicació (*)")
print("4. Divisió (/)")

opcio = input("Introdueix el número de l'operació (1-4): ")

# Realitzar l'operació seleccionada
if opcio == "1":
    resultat = num1 + num2
    print(f"\n{num1} + {num2} = {resultat}")
    
elif opcio == "2":
    resultat = num1 - num2
    print(f"\n{num1} - {num2} = {resultat}")
    
elif opcio == "3":
    resultat = num1 * num2
    print(f"\n{num1} * {num2} = {resultat}")
    
elif opcio == "4":
    if num2 != 0:
        resultat = num1 / num2
        print(f"\n{num1} / {num2} = {resultat}")
    else:
        print("\nERROR: No es pot dividir per zero!")
        
else:
    print("\nOpció no vàlida!")

print("\nFi del programa.")