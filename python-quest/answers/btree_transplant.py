# Write your solution here

def btree_transplant(root, node, replacement):
    sort_root = sorted(root) #temporary sorting, root source remains unchanged
    start_point = 0
    end_point = len(sort_root) - 1
    
    while start_point <= end_point:
        midpoint = start_point + (end_point - start_point) // 2
        mid_value = sort_root[midpoint]

        if node == mid_value:

            original_index = root.index(node)
            root[original_index] = replacement

            return original_index
        
        elif node < mid_value:
            end_point = midpoint - 1

        else: 
            start_point = midpoint + 1

    return None

root_a = [2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10]
node_a = 16
replacement_a = 255

result_index = btree_transplant(root_a, node_a, replacement_a)

if result_index is not None:
    print(f"\033[32mSuccessfully found {node_a} and replaced with {replacement_a} at index {result_index}\033[0m")
else:
    print(f"\033[31m{node_a} was not found — nothing was replaced\033[0m")

print(root_a)





