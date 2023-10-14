import random

random_integers = []

for _ in range(4):
    random_integer = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
    print(random_integer)

# random_integers now contains a list of 4 random 4-digit integers separated by hyphens
