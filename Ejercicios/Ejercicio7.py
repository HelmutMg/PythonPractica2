def num_primos(num):
    if num <= 1:
        return False  

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False 

    return True


number = int(input("Ingresar un número: "))

if num_primos(number):
    print(f"{number} :SI es un número primo.")
else:
    print(f"{number} :NO es un número primo.")
