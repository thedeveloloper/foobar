def solution(n):
    if n % 2 == 0:
        steps = 1
        n -= 1
    else:
        steps = 0

    while n > 1:
        n = n / 2
        steps += 1
    return steps


print(solution(4))