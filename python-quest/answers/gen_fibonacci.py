# # Write your solution here
# def gen_fibonacci(n) :
#     i < n
#     while i <= n:
#         yield i
#         gen_fibonacci(n-1) + gen_fibonacci(n-2)
#     # return result

# print(list(gen_fibonacci(6)))


def gen_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(gen_fibonacci(8)))