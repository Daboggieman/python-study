# Write your solution here
def btree_delete_node(root, node):
    if len(root) > 0:
        sort_root = sorted(root)
    else:
        print("empty root_list")
    start_point = 0
    end_point = len(root) - 1

    if root == None:
        return None
    
    while start_point <= end_point:
        midpoint = start_point + (end_point - start_point) // 2
        mid_value = sort_root[midpoint]
        if node == mid_value:
            del sort_root[midpoint]
        elif node < mid_value:
            end_point = midpoint - 1
        else: 
            start_point = midpoint + 1
    return None

root_a = [2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
node_a = 17

result_index = btree_delete_node(root_a, node_a)

if result_index is not None:
    print(f"\033[32mSuccessfully found and deleted {node_a} at index {result_index}\033[0m")
else:
    print(f"\033[31m{node_a} was not found — nothing was DELETED 033[0m")

print(root_a)