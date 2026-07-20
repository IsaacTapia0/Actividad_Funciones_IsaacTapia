# Verificar si una frase es palíndromo

def es_palindromo(texto):
    texto = texto.lower()
    limpio = ""
    for caracter in texto:
        if caracter.isalnum():
            limpio += caracter
    return limpio == limpio[::-1], limpio

entrada = input("Ingrese una frase: ")

if not entrada.strip():
    print("Error: Debes ingresar una frase.")
else:
    resultado, cadena_limpia = es_palindromo(entrada)

    print(f"\nFrase original: '{entrada}'")
    print(f"Frase limpia: '{cadena_limpia}'")

    if resultado:
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")
