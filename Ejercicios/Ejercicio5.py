def parametros(num, digitos):
    
    number_str = str(num)
    

    cant = number_str.count(str(digitos))
    
    return cant


numero = int(input("Ingresar un número: "))
digito = int(input("Dígito: "))

cantidad= parametros(numero, digito)
print(f"Cantidad de veces que se repite el  {digito} en el número son: {cantidad}")
