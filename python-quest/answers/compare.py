# Write your solution here
first_string = list(input("\033[32m insert the first string: \n \033[0m"))
second_string = list(input("\033[32m insert the second string: \n \033[0m"))

def compare(fir_list, oth_list):
    cop_fir_list = fir_list
    cop_oth_list = oth_list
    while len(cop_fir_list) != len(cop_oth_list):
        if len(cop_fir_list) < len(cop_oth_list):
            cop_fir_list.append(" ")
        else: #len(cop_fir_str) > len(cop_oth_str):
            cop_oth_list.append(" ")
    # print(cop_fir_str)
    # print(cop_oth_str)
    i = 0
    list_of_unidentical = []
    list_of_identical = []
    noncomp = 0
    identical = 0
    while i < len(cop_fir_list):
        if cop_fir_list[i] != cop_oth_list[i]:
            noncomp += 1
            list_of_unidentical.append(i)
            # print(f"unidentical characters found at index {i}")
        else:
            identical += 1
            list_of_identical.append(i)
        i += 1
    print(f"index position(s) of unmatching characters: \033[31m {list_of_unidentical} \033[0m")
    print(f"total numbers of unidentical characters at same indexes: \033[31m {noncomp} \033[0m")
    print(f"index position(s) of matching characters:  \033[32m {list_of_identical} \033[0m")
    print(f"total numbers of identical characters at same indexes: \033[32m {identical} \033[0m")
    # return "whatever it is that u need to return"
compare(first_string, second_string)