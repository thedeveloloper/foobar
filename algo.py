from random import randint


def tobase(n, b):
    digits = []
    return "".join(digits)


def solution(n, b):
    minion_ids = [str(n)]
    loop_start = None
    loop_count = 0

    k = len(str(n))

    while True:
        x = list(str(n))
        x.sort(reverse=True)
        x = int("".join(x))

        y = list(str(n))
        y.sort()
        y = int("".join(y))

        z = str(x - y).zfill(k)

        if z not in minion_ids:
            minion_ids.append(z)
        elif z in minion_ids and not loop_start:
            loop_start = z
            loop_count += 1
        elif z == loop_start:
            return loop_count
        else:
            loop_count += 1
        n = z


print(solution(1211, 3))