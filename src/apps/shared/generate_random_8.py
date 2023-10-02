import random


def generate_random_8():
    number = "".join(str(random.randint(0, 9)) for _ in range(8))
    return int(number)
