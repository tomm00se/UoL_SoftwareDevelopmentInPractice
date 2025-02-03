import random

def generate_random_number(start, end):
    return random.randint(start, end)

random_number  = generate_random_number(1, 100)
print(f"Random number between 1 and 100: {random_number}")