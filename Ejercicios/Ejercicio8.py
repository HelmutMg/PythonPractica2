def num_factorial(number):
    if number < 0:
        return "El factorial no está definido para números negativos."
    elif number == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return factorial


num = int(input("Ingresar un número no negativo: "))

result = num_factorial(num)
print(f"El factorial de {num} es: {result}")
