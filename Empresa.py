import random
import csv

trabajadores = [
    "Juan Pérez",
    "María García",
    "Pedro Soto",
    "Isabel Gómez",
    "Miguel Sánchez",
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
        # Clasificar sueldos según las categorías especificadas
        menores_800k = []
        entre_800k_2m = []
        superiores_2m = []

        for trabajador, salario in diccionario_salarios.items():
            if salario < 800000:
                menores_800k.append((trabajador, salario))
            elif 800000 <= salario <= 2000000:
                entre_800k_2m.append((trabajador, salario))
            elif salario > 2000000:
                superiores_2m.append((trabajador, salario))

        # Mostrar resultados
        print(f"Sueldos menores a $800,000 TOTAL: {len(menores_800k)}")
        print("Nombre empleado Sueldo")
        for nombre, sueldo in menores_800k:
            print(f"{nombre} ${sueldo}")

        print(f"\nSueldos entre $800,000 y $2,000,000 TOTAL: {len(entre_800k_2m)}")
        print("Nombre empleado Sueldo")
        for nombre, sueldo in entre_800k_2m:
            print(f"{nombre} ${sueldo}")

        print(f"\nSueldos superiores a $2,000,000 TOTAL: {len(superiores_2m)}")
        print("Nombre empleado Sueldo")
        for nombre, sueldo in superiores_2m:
            print(f"{nombre} ${sueldo}")

        # Mostrar el total de sueldos
        total_sueldos = sum(diccionario_salarios.values())
        print(f"\nTOTAL SUELDOS: ${total_sueldos}")

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
        print("Ojala allamos sido de ayuda ",  nombre, Rut)
        break 

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
