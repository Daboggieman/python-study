# Write your solution here
def count_if(predicate, items) :
    if len(items) < 1 :
        print("items list is empty")
        return None
    check =list(map(predicate, items))
    count = 0
    for j in check :
        if j == True :
            count += 1
    return count, check

# the function is to take the 2 arguments passed through it 
# and check for how many of the items in the second arguments list satisfies the condition in the first argument
# and returns the amount of times the condition is satisfied through out the list of second argument

print(count_if(lambda x: x > 2, [1, 2, 3, 4]))