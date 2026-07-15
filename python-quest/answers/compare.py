# Write your solution here
first_string = list(input("\033[32m insert the first string: \n \033[0m"))
second_string = list(input("\033[32m insert the second string: \n \033[0m"))

def compare(fir_str, oth_str):
    while len(fir_str) != len(oth_str):
        if len(fir_str) < len(oth_str):
            fir_str.append(" ")
        else: #len(fir_str) > len(oth_str):
            oth_str.append(" ")
    # print(fir_str)
    # print(oth_str)
    


compare(first_string, second_string)