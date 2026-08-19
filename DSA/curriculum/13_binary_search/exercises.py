# DSA Exercise 13: Binary Search
# Run this script with: python exercises.py


# TODO: Exercise 1 - iterative binary search, return index or -1
def binary_search(arr, target):
    sort_arr = sorted(arr)
    startpoint = sort_arr[0]
    endpoint = sort_arr[len(sort_arr)-1]

    while startpoint <= endpoint:
        midpoint = startpoint + (endpoint-startpoint) // 2
        midvalue = sort_arr[midpoint]

# after successfully calculating midpoint, then proceed to check if the midpoint is equal the value of the target
        if midpoint is target:
            return midpoint
        elif midpoint < target:
            endpoint = midpoint - 1
        else:
            endpoint = midpoint + 1
    return None


# TODO: Exercise 2 - recursive binary search, return index or -1
def binary_search_recursive(arr, target, low=0, high=None):
    # find a target in an array with no le
    pass


# TODO: Exercise 3 - reimplement bisect_left: return the index where
# `target` would be inserted to keep `arr` sorted (target may not be present)
def bisect_left_manual(arr, target):
    pass


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(data, 7))              # 3
    print(binary_search(data, 4))              # -1
    print(binary_search_recursive(data, 11))   # 5
    print(bisect_left_manual(data, 6))         # 3 (would go between 5 and 7)
