import string


def encryption(input, encrypt):
    alpha = string.ascii_lowercase
    rev_alpha = alpha[::-1]
    trans = (
        input.maketrans(alpha, rev_alpha)
        if encrypt
        else input.maketrans(rev_alpha, alpha)
    )
    return input.translate(trans)


print(
    encryption(
        "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!", encrypt=False
    )
)
