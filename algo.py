def solution(n, b):
    minion_ids = [str(n)]
    loop_start = None
    loop_count = 0

    k = len(str(n))

    while True:
        x = list(str(n))
        x.sort(reverse=True)
        x = "".join(x)

        y = list(str(n))
        y.sort()
        y = "".join(y)

        digits = []
        ans = int(x, b) - int(y, b)

        while ans > 0:
            digits.insert(0, str(ans % b))
            ans = ans // b

        z = "".join(digits).zfill(k)

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


print(solution(210022, 3))

# 10 = (n-1, 1) (n-2, 2) ((n-3, 3) (n-3, 2, 1)) ((n-4, 4) (n-4, 3, 1)) ((n-5, 4, 1) (n-5, 3, 2)) (n-6, 3, 2, 1)