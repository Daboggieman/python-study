# Write your solution here
def btree_search_item(root, value):
    sort_root = sorted(root)
    start_point = 0
    end_point = len(root) - 1
    
    while start_point <= end_point:
        midpoint = start_point + (end_point - start_point) // 2
        mid_value = sort_root[midpoint]
        if value == mid_value:
            return midpoint
        elif value < mid_value:
            end_point = midpoint - 1
        else: 
            start_point = midpoint + 1
    return None

root_a = [2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
value_a = 16

print(f"\033[032m{value_a} found at index {btree_search_item(root_a, value_a)}\033[0m")