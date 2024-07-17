import random

def generate_random_balances(num_accounts):
    return [random.randint(300.000, 2500000) for _ in range(num_accounts)]

print("Bienvenido a ")