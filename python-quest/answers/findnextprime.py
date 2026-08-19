# Write your solution here
#find the next prime number, greater to or even to the provided number

def find_next_prime(n) :
    i = n
    while n :
        if i % 2 != 0 or i % 3 != 0 or i % 5 != 0 :
            return i
            break
        else:
            i += 1
    return i

print(find_next_prime(10))