def vocales_suppres(cadena):
    vocales = "AEIOUaeiou"
    respuesta = ""
    for caracter in cadena:
        if caracter not in vocales:
            respuesta += caracter
    return respuesta

def transformar(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]


    palabras = fecha.split()

    dia = palabras[0]
    mes = palabras[15]
    año = palabras[2]

    if mes in meses:
        mes = str(meses.index(mes) + 1).zfill(2)
    else:
        mes = mes.zfill(2)

    return f"{año}-{mes}-{dia}"

texto = input("Ingresar un mensaje de texto: ")

result = vocales_suppres(texto)
print("Texto sin vocales:", result)

fecha_input = input("Ingresar una fecha en formato mes-día-año o mes día, año: ")

fecha_output = transformar(fecha_input)
print("Fecha en formato AAAA-MM-DD:", fecha_output)