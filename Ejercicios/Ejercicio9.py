def vocales_suppress(cadena):

    vocales = "AEIOUaeiou"
    
    respuesta = ""
    
    for caracter in cadena:
        if caracter not in vocales:
            respuesta += caracter
    
    return respuesta

text = input("Ingresar una oración de palabras: ")

result = vocales_suppress(text)
print("Texto sin vocales:", result)
