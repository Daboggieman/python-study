# Write your solution here
def map_values(predicate, item_list):
    if len(item_list) < 1 :
        return "Item list is Empty"
    check_items = list(map(predicate, item_list))
    bool_list = []

    for conditions in check_items:
        bool_list.append(conditions)
    return bool_list

print(map_values(lambda x: x > 3, [6, 1, 2 , 3, 4, 6, 0]))