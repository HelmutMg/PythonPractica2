num_filas = 5

for i in range(1, num_filas + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

for i in range(num_filas - 1, 0, -1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()
