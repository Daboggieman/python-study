# Write your solution here
def foreach(predicate, lists) :
    results = list(map(predicate, lists))
    print(results)

foreach(lambda x: x * 2, [1, 2, 3, 4, 5]),
#predicate, and list, on index[0], and index[1]