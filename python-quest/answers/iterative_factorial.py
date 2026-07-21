# Write your solution here
def iterative_factorial(n):
    if n < 1 :
        return 0
    if n == 1:
        return 1 
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(iterative_factorial(5))