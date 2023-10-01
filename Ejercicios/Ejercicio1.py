num_divisible = []

for numero in range(1500, 2701):
 
    if numero % 7 == 0 and numero % 5 == 0:
        
        num_divisible.append(numero)

print("Numeros divisibles por 7 y múltiplos de 5 en el rango de <1500 a 2700> son:")
print(num_divisible)
