import random

def generate_random_balances(num_accounts):
    return [random.randint(300.000, 2500000) for _ in range(num_accounts)]

print("Bienvenido al menu de Opciones")
print("1. Asignar sueldos aleatorios")
print("2. Clasificar sueldos")
print("3. Ver estadísticas.")
print("4. Reporte de sueldos")
print("5. Salir del programa")
