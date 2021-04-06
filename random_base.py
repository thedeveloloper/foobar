from random import randint


def random_base(n, b):
    rand_int = ""
    for num in range(n):
        del num
        rand_int = f"{rand_int}{randint(0, b - 1)}"

    return rand_int.zfill(n)


print(random_base(5, 2))