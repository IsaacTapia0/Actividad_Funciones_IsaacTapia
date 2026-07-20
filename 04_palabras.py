# Convertir palabras a mayúsculas

def procesar_palabra(palabra):
    return palabra.upper()

def main():
    print("Ingresa palabras (Enter vacío para terminar)")
    contador = 0

    while True:
        entrada = input("Palabra: ")

        if entrada == "":
            break

        resultado = procesar_palabra(entrada)
        print(f"  -> {resultado}")
        contador += 1

    print(f"\nPrograma terminado. Palabras procesadas: {contador}")

main()
