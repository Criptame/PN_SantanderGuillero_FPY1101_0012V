import random
import csv

trabajadores = [
    "Jose Alvaro",
    "Maria Isabel",
    "Pedro Pablo",
    "Juan Ignacio",
    "Antonio José",
    "Sofia Maria",
]

def generate_random_balances(num_accounts):
    return [random.randint(30000, 2500000) for _ in range(num_accounts)]

salarios = generate_random_balances(len(trabajadores))

diccionario_salarios = dict(zip(trabajadores, salarios))

nombre = input("Escriba su nombre: ")
Rut = input("Digite su Rut: ")

print(f"Bienvenido al menu de Opciones {nombre}")
print("1. Asignar sueldos aleatorios a trabajadores")
print("2. Clasificar sueldos, Entre mayor, menor o igual ")
print("3. Ver estadísticas ")
print("4. Reporte de sueldos")
print("5. Salir del programa")

while True:
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        for trabajador, salario in diccionario_salarios.items():
            print(f"{trabajador}: ${salario}")

    elif opcion == '2':
        sorted_salarios = sorted(diccionario_salarios.items(), key=lambda x: x[1], reverse=True)
        print("Lista de salarios ordenados de mayor a menor:")
        for trabajador, salario in sorted_salarios:
            print(f"{trabajador}: ${salario}")

    elif opcion == '3':
        total_salarios = sum(diccionario_salarios.values())
        promedio_salarios = total_salarios / len(trabajadores)
        salario_maximo = max(diccionario_salarios.values())
        salario_minimo = min(diccionario_salarios.values())
        
        print(f"Promedio de salarios: ${promedio_salarios}")
        print(f"Salario máximo: ${salario_maximo}")
        print(f"Salario mínimo: ${salario_minimo}")

    elif opcion == '4':
        with open('reporte_salarios.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Trabajador', 'Salario'])
            for trabajador, salario in diccionario_salarios.items():
                writer.writerow([trabajador, salario])
        print("Reporte de salarios generado correctamente.")

    elif opcion == '5':
        print("Saliendo del programa...")
        break 

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
