# Write your solution here
string_list_a = list(input("insert the list to sort through, seperate by comma: \n"))
without_a = input("insert the characted/word to deduct count from the list: \n")
def compact(string_list, without):
    if len(string_list) < 1:
        print("list is empty")
        return []
    count = 0
    i = 0
    while i < len(string_list):
        if string_list[i] != without:
            count += 1
        i += 1
    return count
    print(f"the lenght of the list is {len(string_list)} \n")

print(f"and there are {compact(string_list_a, without_a)} indexes without '{without_a}'")