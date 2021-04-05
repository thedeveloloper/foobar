import string


def solution(s):
    alpha = string.ascii_lowercase
    rev_alpha = alpha[::-1]
    trans = s.maketrans(rev_alpha, alpha)
    return s.translate(trans)


print(solution("aaaaaaaaAaaaaaa"))