import random
import csv
import math

trabajadores = [
    "Juan Pérez",
    "María García",
    "Pedro Soto",
    "Isabel Gómez",
    "Miguel Sánchez",
]

def generate_random_balances(num_accounts):
    return [random.randint(30000, 2500000) for _ in range(num_accounts)]

def actualizar_sueldos():
    global diccionario_salarios
    salarios = generate_random_balances(len(trabajadores))
    diccionario_salarios = dict(zip(trabajadores, salarios))

def calcular_descuento_salud(sueldo):
    return sueldo * 0.07

def calcular_descuento_afp(sueldo):
    return sueldo * 0.12

def calcular_sueldo_liquido(sueldo_base):
    descuento_salud = calcular_descuento_salud(sueldo_base)
    descuento_afp = calcular_descuento_afp(sueldo_base)
    sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
    return sueldo_liquido, descuento_salud, descuento_afp

nombre = input("Escriba su nombre: ")
Rut = input("Digite su Rut: ")

print(f"Bienvenido al menu de Opciones {nombre}")
print("1. Asignar sueldos aleatorios a trabajadores")
print("2. Clasificar sueldos")
print("3. Ver estadísticas ")
print("4. Reporte de salarios")
print("5. Calcular sueldo líquido y aplicar descuentos")
print("6. Salir del programa")

while True:
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        actualizar_sueldos()
        print("Sueldos actualizados aleatoriamente.")

    elif opcion == '2':
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

        total_sueldos = sum(diccionario_salarios.values())
        print(f"\nTOTAL SUELDOS: ${total_sueldos}")

    elif opcion == '3':
        if not diccionario_salarios:
            print("No hay datos de sueldos. Por favor, asigna sueldos primero (opción 1).")
            continue
        
        sueldos = list(diccionario_salarios.values())
        
        sueldo_maximo = max(sueldos)
        sueldo_minimo = min(sueldos)
        promedio_sueldos = sum(sueldos) / len(sueldos)
        media_geometrica = math.prod(sueldos) ** (1 / len(sueldos))

        print(f"Sueldo más alto: ${sueldo_maximo}")
        print(f"Sueldo más bajo: ${sueldo_minimo}")
        print(f"Promedio de sueldos: ${promedio_sueldos}")
        print(f"Media geométrica de sueldos: ${media_geometrica}")

    elif opcion == '4':
        with open('reporte_salarios.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Trabajador', 'Salario'])
            for trabajador, salario in diccionario_salarios.items():
                writer.writerow([trabajador, salario])
        print("Reporte de salarios generado correctamente.")

    elif opcion == '5':
        print("Calculando sueldos líquidos y aplicando descuentos...")
        print("Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo Líquido")
        for trabajador, sueldo_base in diccionario_salarios.items():
            sueldo_liquido, descuento_salud, descuento_afp = calcular_sueldo_liquido(sueldo_base)
            print(f"{trabajador} ${sueldo_base} ${descuento_salud} ${descuento_afp} ${sueldo_liquido}")

    elif opcion == '6':
        print("Saliendo del programa, Ojala alla sido de ayuda")
        print("Desarrolado por", nombre)
        print("Rut", Rut)
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")