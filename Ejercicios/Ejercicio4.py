list_alumnos = []

n = int(input("Ingresar la cantidad de alumnos: "))

for i in range(n):
    student = input("Ingresar el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresar la calificación  {j + 1} para {student}: "))
        notas.append(nota)
    
    student_info = {
        "Student": student,
        "Notas": notas
    }
    
    list_alumnos.append(student_info)

print("\nLista completo de alumnos:")
for student_info in list_alumnos:
    print(f"Alumno: {student_info['Student']}, Notas: {student_info['Notas']}")
