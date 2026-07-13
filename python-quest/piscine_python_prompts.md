# Python Piscine-style Questions

These prompts were translated from Go exercise files in the Piscine repo and rewritten as Python-style questions.

## Batch 1: first 20 files

1. From `abort.go`: Write a function `abort(a, b, c, d, e)` that returns the middle value of five integers after sorting them.
2. From `activebits.go`: Write a function `active_bits(n)` that returns the number of `1` bits in the binary representation of `n`.
3. From `advancedsortwordarr.go`: Write a function `advanced_sort_word_arr(words, cmp)` that sorts a list of strings using a custom comparison function.
4. From `any.go`: Write a function `any_value(predicate, items)` that returns `True` if at least one item makes the predicate return `True`.
5. From `appendrange.go`: Write a function `append_range(min_value, max_value)` that returns a list of integers from `min_value` up to but not including `max_value`.
6. From `atoibase.go`: Write a function `atoi_base(s, base)` that converts a number written in a custom base into an integer.
7. From `atoi.go`: Write a function `atoi(s)` that converts a numeric string into an integer, returning `0` if the conversion fails.
8. From `basicatoi2.go`: Write a function `basic_atoi2(s)` that converts a numeric string into an integer, returning `0` if it is invalid.
9. From `basicatoi.go`: Write a function `basic_atoi(s)` that converts a numeric string into an integer, returning `0` if it is invalid.
10. From `basicjoin.go`: Write a function `basic_join(items)` that joins all strings in a list into one string.
11. From `boolean/main.go`: Write a program that prints whether the number of command-line arguments is even or odd.
12. From `btreeapplybylevel.go`: Write a function `btree_apply_by_level(root, fn)` that applies a callback to each node in a binary tree level by level.
13. From `btreeapplyinorder.go`: Write a function `btree_apply_inorder(root, fn)` that traverses a binary tree in-order and applies a callback to each node.
14. From `btreeapplypostorder.go`: Write a function `btree_apply_postorder(root, fn)` that traverses a binary tree post-order and applies a callback to each node.
15. From `btreeapplypreorder.go`: Write a function `btree_apply_preorder(root, fn)` that traverses a binary tree pre-order and applies a callback to each node.
16. From `btreedeletenode.go`: Write a function `btree_delete_node(root, node)` that removes a node from a binary search tree and returns the updated root.
17. From `btreeinsertdata.go`: Write a function `btree_insert_data(root, data)` that inserts a value into a binary search tree.
18. From `btreeisbinary.go`: Write a function `btree_is_binary(root)` that checks whether a tree is a valid binary search tree.
19. From `btreelevelcount.go`: Write a function `btree_level_count(root)` that returns the height or number of levels of a binary tree.
20. From `btreemax.go`: Write a function `btree_max(root)` that returns the node with the maximum value in a binary search tree.

## Batch 2: next 30 files

21. From `capitalize.go`: Write a function `capitalize(s)` that transforms a string by capitalizing the first letter of each word separated by underscores and lowercasing the rest.
22. From `cat/main.go`: Write a program that reads one or more files given as command-line arguments and prints their contents to the screen.
23. From `collatz.go`: Write a function `collatz_countdown(start)` that returns the number of steps needed to reach `1` using the Collatz sequence.
24. From `comcheck/main.go`: Write a program that prints an alert message when one of a few specific arguments is passed.
25. From `compact.go`: Write a function `compact(strings_list, length)` that counts how many non-space elements are present in a list.
26. From `compare.go`: Write a function `compare(s, other)` that compares two strings and returns the result of the comparison.
27. From `concat.go`: Write a function `concat(a, b)` that joins two strings together.
28. From `concatparams.go`: Write a function `concat_params(args)` that joins a list of arguments into one string, separating them with newlines.
29. From `convertbase.go`: Write a function `convert_base(number, base_from, base_to)` that converts a number from one base to another.
30. From `countdown.go`: Write a program or function that prints the numbers from `9` down to `1`.
31. From `countif.go`: Write a function `count_if(predicate, items)` that counts how many elements satisfy the predicate.
32. From `displaya.go`: Write a program that prints the letter `a` followed by a newline.
33. From `displayfile/main.go`: Write a program that reads and prints the contents of a file, with proper handling for missing or too many arguments.
34. From `displayz.go`: Write a program or function that prints the letter `z` and a newline.
35. From `divmod.go`: Write a function `div_mod(a, b)` that returns both the quotient and remainder of integer division.
36. From `doop/main.go`: Write a program that performs basic arithmetic on two integers based on an operator.
37. From `eightqueens.go`: Write a program that solves the eight queens puzzle and prints one valid placement.
38. From `enigma.go`: Write a function that swaps values between several pointers in a chained way.
39. From `fibonacci.go`: Write a function `fibonacci(n)` that returns the nth Fibonacci number.
40. From `findnextprime.go`: Write a function `find_next_prime(n)` that returns the next prime number greater than or equal to `n`.
41. From `firstrune.go`: Write a function `first_rune(s)` that returns the first character of a string.
42. From `fixthemain/main.go`: Write a small program that models a door that can be opened and closed using functions.
43. From `foreach.go`: Write a function `for_each(func, items)` that applies a function to every item in a list.
44. From `hello.go`: Write a program that prints `Hello World!`.
45. From `index.go`: Write a function `index_of(text, sub)` that returns the index of a substring in a string.
46. From `isalpha.go`: Write a function `is_alpha(s)` that checks whether a string contains only letters, digits, or underscores.
47. From `islower.go`: Write a function `is_lower(s)` that checks whether all letters in a string are lowercase.
48. From `isnegative.go`: Write a function `is_negative(n)` that prints `T` for negative numbers and `F` otherwise.
49. From `isnumeric.go`: Write a function `is_numeric(s)` that checks whether a string contains only digits or underscores.
50. From `isprime.go`: Write a function `is_prime(n)` that checks whether a number is prime.

## Batch 3: next 24 files

51. From `isprintable.go`: Write a function `is_printable(s)` that returns `True` if all characters in the string are printable.
52. From `issorted.go`: Write a function `is_sorted(compare, values)` that returns `True` if a list is sorted in ascending or descending order according to a custom comparison function.
53. From `isupper.go`: Write a function `is_upper(s)` that returns `True` if all letters in the string are uppercase.
54. From `iterativefactorial.go`: Write a function `iterative_factorial(n)` that computes the factorial of a number using iteration.
55. From `iterativepower.go`: Write a function `iterative_power(base, exp)` that computes `base` raised to `exp` using iteration.
56. From `join.go`: Write a function `join(items, separator)` that joins a list of strings using a separator.
57. From `lastrune.go`: Write a function `last_rune(s)` that returns the last character of a string.
58. From `listat.go`: Write a function `list_at(linked_list, pos)` that returns the node at a given position in a linked list.
59. From `listclear.go`: Write a function `list_clear(linked_list)` that empties a linked list.
60. From `listfind.go`: Write a function `list_find(linked_list, value, comp)` that finds a value in a linked list using a custom comparison function.
61. From `listforeach.go`: Write a function `list_for_each(linked_list, action)` that applies a function to every node in a linked list.
62. From `listforeachif.go`: Write a function `list_for_each_if(linked_list, action, condition)` that applies an action only to nodes that satisfy a condition.
63. From `listlast.go`: Write a function `list_last(linked_list)` that returns the last value stored in a linked list.
64. From `listmerge.go`: Write a function `list_merge(list1, list2)` that appends the second linked list to the end of the first.
65. From `listpushback.go`: Write a function `list_push_back(linked_list, data)` that adds a node to the end of a linked list.
66. From `listpushfront.go`: Write a function `list_push_front(linked_list, data)` that adds a node to the beginning of a linked list.
67. From `listremoveif.go`: Write a function `list_remove_if(linked_list, value)` that removes all nodes matching a given value.
68. From `listreverse.go`: Write a function `list_reverse(linked_list)` that reverses the order of nodes in a linked list.
69. From `listsize.go`: Write a function `list_size(linked_list)` that returns the number of nodes in a linked list.
70. From `listsort.go`: Write a function `list_sort(linked_list)` that sorts a linked list of integers.
71. From `makerange.go`: Write a function `make_range(min_value, max_value)` that returns a list of integers from `min_value` up to but not including `max_value`.
72. From `map.go`: Write a function `map_values(predicate, values)` that applies a predicate to each item and returns a list of booleans.
73. From `max.go`: Write a function `max_value(values)` that returns the largest integer in a list.
