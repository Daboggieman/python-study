# Write your solution here

def collatz_countdown(s):
    if s == 1 :
        return 1
    elif s < 1:
        print ("invalid value cannot collatz values less than 1")
        return None
    i = 0
    while s > 1:
        if s % 2 == 0:
            s = s / 2
        else:
            s = (3 * s) + 1
        # print(s)
        i += 1
    return i
print(collatz_countdown(12))
        