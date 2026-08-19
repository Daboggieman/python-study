# Write your solution here
def divmod(a, b) :
    result = []

    if a == 0 :
        return "cannot divide zero(0)"
    elif b == 0 :
        return "cannot divide by zero (0)"
    else:
        result.append(a // b)
        result.append(a % b)

    return result[0], result[1]


answer = divmod(13, 2)
print(answer[0])
print(answer[1])

