import random


def generate_random_8(prefix: str = 'ST'):
    number = "".join(str(random.randint(0, 9)) for _ in range(8))
    return prefix + str(number)
