import string


def solution(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    rev_alpha = alpha[::-1]
    trans = string.maketrans(rev_alpha, alpha)
    return s.translate(trans)


temp = solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
print(temp)