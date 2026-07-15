# Write your solution here
def basic_join(items):
    result = ''
    if len(items) == 0:
        print("ERROR: the list is EMPTY")
    else:
        i = 0
        while i <= len(items) - 1:
            result += (items[i] + " ")
            i += 1
        print(result + "\n" )
basic_join(["these", "are", "the", "items", "to", "concantenate"])
basic_join([])