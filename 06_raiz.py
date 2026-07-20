# Calcular raíz cuadrada con método de Newton

import math

def raiz_newton(n, tolerancia=1e-10):
    if n < 0:
        return None
    if n == 0:
        return 0
    estimacion = n / 2.0
    while True:
        nueva = 0.5 * (estimacion + n / estimacion)
        if abs(nueva - estimacion) < tolerancia:
            return nueva
        estimacion = nueva

try:
    num = float(input("Número: "))

    if num < 0:
        print("Error: No se puede calcular raíz de un número negativo.")
    else:
        r1 = math.sqrt(num)
        r2 = raiz_newton(num)

        print(f"\nRaíz cuadrada de {num}:")
        print(f"  math.sqrt: {r1}")
        print(f"  Newton: {r2:.10f}")

        if abs(r1 - r2) < 1e-9:
            print("  Los resultados coinciden.")

except ValueError:
    print("Error: Ingresa un número válido.")
