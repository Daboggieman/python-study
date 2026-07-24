# Write your solution here
def basic_atoi(s):
    if s.isdigit():
        return int(s)
    else:
        return 0
    
print(basic_atoi("42"))
print(basic_atoi("x"))