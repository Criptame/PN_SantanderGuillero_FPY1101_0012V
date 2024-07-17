import random

def generate_random_balances(num_accounts):
    return [random.randint(300.000, 2500000) for _ in range(num_accounts)]

trabajadores = [
    "Jose Alvaro",
    "Maria Isabel",
    "Pedro Pablo",
    "Juan Ignacio",
    "Antonio José",
    "Sofia Maria",
]


nombre = input("Escriba su nombre: ")  
Rut = input("Digite su Rut: ") 

print(f"Bienvenido al menu de Opciones {nombre}")
print("1. Asignar sueldos aleatorios y mostar")
print("2. Clasificar sueldos ")
print("3. Ver estadísticas y mostar")
print("4. Reporte de sueldos y mostar")
print("5. Salir del programa y mostar")


while True:
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        num_accounts = int(input("Ingrese el número de cuentas: "))
        balances = generate_random_balances(num_accounts)
        print(f"Balances generados aleatorios para {num_accounts} cuentas:")
        for i, balance in enumerate(balances, start=1):
            print(f"Cuenta {i}: ${balance}")