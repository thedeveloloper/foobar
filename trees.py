def solution(h, q):
    result = []

    for node in q:
        start = 1
        end = (2 ** h) - 1
        if node == end:
            result.append(-1)
        else:
            while node >= 1:
                end = end - 1
                mid = start + (end - start) // 2
                if mid == node or end == node:
                    result.append(end + 1)
                    break
                elif node < mid:
                    end = mid
                else:
                    start = mid
    return result


print(solution(5, [19, 14, 28]))


# searching from 1 to (2**h)-1