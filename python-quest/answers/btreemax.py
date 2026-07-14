# Write your solution here

def btree_max(node):
    if len(node) == 0:
        print("node list is empty")
        return None
    current_node = node[0]
    max_node = current_node
    i = 1
    while i <= len(node) - 1:
        if max_node > node[i]:
            max_node = max_node
        else:
            max_node = node[i]
        i += 1
    print(f"the maximum value in the node is \033[32m{max_node}\033[0m")
    return max_node
    
btree_max([-4, 5, 7, 2, 23, 1, -7, 1, 6])