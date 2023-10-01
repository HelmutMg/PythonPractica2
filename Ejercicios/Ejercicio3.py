num_par = []
num_impar = []

while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()

    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        if numero % 2 == 0:
            num_par.append(numero)
        else:
            num_impar.append(numero)
    elif respuesta == "NO":
        break
    else:
        print("Respuesta no válida. Por favor, responda con 'SI' o 'NO'.")

print("Numeros ingresados:", num_par + num_impar)
print("Cantidad de números pares:", len(num_par))
print("Cantidad de números impares:", len(num_impar))
