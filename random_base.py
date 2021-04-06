from random import randint
from string import ascii_uppercase


def random_base(n, b):
    rand_int = ""
    alpha = ascii_uppercase
    for num in range(n):
        if num >= 10:
            num = alpha[num - 9]
            print(alpha[num - 9])
        rand_int = f"{rand_int}{randint(0, b - 1)}"

    return rand_int.zfill(n)


print(random_base(5, 12))