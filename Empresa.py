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

# Función para generar sueldos aleatorios
def generate_random_balances(num_accounts):
    return [random.randint(30000, 2500000) for _ in range(num_accounts)]

# Función para actualizar los sueldos de los trabajadores
def actualizar_sueldos():
    global diccionario_salarios
    salarios = generate_random_balances(len(trabajadores))
    diccionario_salarios = dict(zip(trabajadores, salarios))
    guardar_en_csv()

# Función para calcular el descuento de salud
def calcular_descuento_salud(sueldo):
    return sueldo * 0.07

# Función para calcular el descuento de AFP
def calcular_descuento_afp(sueldo):
    return sueldo * 0.12

# Función para calcular el sueldo líquido
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

# Función para guardar los datos en el archivo CSV
def guardar_en_csv():
    with open('reporte_salarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Trabajador', 'Sueldo'])
        for trabajador, salario in diccionario_salarios.items():
            writer.writerow([trabajador, salario])

while True:
    opcion = input("Seleccione una opción (1-6): ")

    if opcion == '1':
        actualizar_sueldos()
        print("Sueldos actualizados aleatoriamente.")

    elif opcion == '2':
        # Código para clasificar sueldos
        # ...
        pass

    elif opcion == '3':
        # Código para ver estadísticas
        # ...
        pass

    elif opcion == '4':
        # Generar reporte de salarios
        guardar_en_csv()
        print("Reporte de salarios generado correctamente.")

    elif opcion == '5':
        # Calcular sueldo líquido y aplicar descuentos
        print("Calculando sueldos líquidos y aplicando descuentos...")
        print("Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo Líquido")
        for trabajador, sueldo_base in diccionario_salarios.items():
            sueldo_liquido, descuento_salud, descuento_afp = calcular_sueldo_liquido(sueldo_base)
            print(f"{trabajador} ${sueldo_base} ${descuento_salud} ${descuento_afp} ${sueldo_liquido}")

    elif opcion == '6':
        # Salir del programa
        print("Saliendo del programa")
        print("Desarrollado por", nombre)
        print("Rut", Rut)
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
