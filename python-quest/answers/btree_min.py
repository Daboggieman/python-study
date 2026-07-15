# Write your solution here
def btree_min(node):
    if len(node) == 0:
        print("\033[32mnode list is empty \033[0m")
        return None
    current_node = node[0]
    smallest_node = current_node
    i = 1
    while i <= len(node) - 1:
        if smallest_node < node[i]:
            smallest_node = smallest_node
        else:
            smallest_node = node[i]
        i += 1
    print(f"the smallest value in the node is \033[32m{smallest_node}\033[0m")
    return smallest_node
    
btree_min([-4, 5, 7, 2, 1, -7, 1, 6])