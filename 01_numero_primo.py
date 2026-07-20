# Verificar si un número es primo

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Ingrese un número: "))

    if num < 0:
        print("Por favor ingresa un número positivo.")
    elif es_primo(num):
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")

except ValueError:
    print("Error: Ingresa un número válido.")
