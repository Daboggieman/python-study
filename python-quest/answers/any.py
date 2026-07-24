# Write your solution here
def any_value(predicate, list_items):
    if not isinstance (list_items, list) :
        list_items = [list_items]

    check_through = list(map(predicate, list_items))
    
    true_count = 0
    
    for j in check_through :
        if j == True:
            true_count += 1
    
    if true_count > 0 :
        return True
    else:
        return False
    
# print(any_value(lambda x: x > 2, [1, 2]))

print(any_value(lambda x: x < 8, [1, 2, 3, 4, 5, 6]))