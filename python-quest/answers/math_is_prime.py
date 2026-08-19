import math

def is_prime(n):
    if n < 2:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            return False
    return True

print(is_prime(17))
print(is_prime(18))
print(is_prime(2))
print(is_prime(1))