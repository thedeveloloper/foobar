from random import randint


def solution(n, b):
    k = len(str(n))
    rand_int = ""
    for num in range(k):
        del num
        rand_int = f"{rand_int}{randint(0, b - 1)}"

    rand_id = rand_int.zfill(k)

    x = list(rand_id)
    x.sort(reverse=True)
    x = "".join(x).zfill(k)

    y = list(rand_id)
    y.sort()
    y = "".join(y).zfill(k)

    z = str(int(x) - int(y)).zfill(k)

    return z


solution(210022, 3)
# print(solution(1001, 10))