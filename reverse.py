from string import ascii_lowercase


def decode(input):
    alpha = ascii_lowercase
    rev_alpha = ascii_lowercase[::-1]
    output = ""
    for c in input:
        if c == " ":
            output.append(c)
        for a in alpha:
            if c == a:
                output.append(rev_alpha[a])

    return output.join()


print(decode("test"))