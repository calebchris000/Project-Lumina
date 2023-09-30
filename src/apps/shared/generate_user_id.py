import random


def generate_user_id():
    number = "".join(str(random.randint(0, 9)) for _ in range(10))
    return int(number)
