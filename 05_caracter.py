# Reemplazar caracteres en una cadena

def reemplazar_manual(texto, viejo, nuevo):
    resultado = ""
    contador = 0

    for letra in texto:
        if letra == viejo:
            resultado += nuevo
            contador += 1
        else:
            resultado += letra

    return resultado, contador

texto = input("Cadena: ")

if not texto:
    print("Error: Debes ingresar una cadena.")
else:
    car_viejo = input("Carácter a reemplazar: ")
    car_nuevo = input("Carácter nuevo: ")

    if len(car_viejo) != 1 or len(car_nuevo) != 1:
        print("Error: Debe ser un solo carácter.")
    else:
        texto_mod, reemplazos = reemplazar_manual(texto, car_viejo, car_nuevo)

        print(f"\nOriginal: '{texto}'")
        print(f"Modificado: '{texto_mod}'")
        print(f"Reemplazos realizados: {reemplazos}")
