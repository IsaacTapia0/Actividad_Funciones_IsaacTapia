# Calcular Máximo Común Divisor

import math

def mcd(a, b):
    a = abs(a)
    b = abs(b)
    if a == 0 and b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a

try:
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))

    resultado = mcd(num1, num2)
    resultado_math = math.gcd(num1, num2)

    print(f"\nMCD de {num1} y {num2}:")
    print(f"  Calculado: {resultado}")
    print(f"  Con math.gcd: {resultado_math}")

    if resultado == resultado_math:
        print("  Los resultados coinciden.")

except ValueError:
    print("Error: Ingresa números válidos.")
