def solution(n):
    num = int(n)
    operations = 0

    if num == 0:
        return 1
    if num < 0:
        num = num * -1
        operations = 2

    while num != 1:
        if num & 1:
            if num & 2 and num != 3:
                num += 1
            else:
                num -= 1
        else:
            num //= 2

        operations += 1

    return operations


print(solution(4))