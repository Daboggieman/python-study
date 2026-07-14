def atoibase(number, base):
    value = 0
    for ch in number:
        if ch >= '0' and ch <= '9':
            digit = ord(ch) - ord('0')
        else:
            digit = ord(ch.upper()) - ord('A') + 10

        if digit < 0 or digit >= base:
            return 0

        value = value * base + digit

    return value
    # print(value)

print(atoibase("101", 2))