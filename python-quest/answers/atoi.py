# Write your solution here
def atoi(n):
    if n.isdigit() :
        return int(n)
    else:
        return 0
        
print(atoi("123"))
print(atoi("abc"))