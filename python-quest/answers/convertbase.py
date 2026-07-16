# Write your solution here
def ask_input():
    base_from = int(input("\033[32m what is the number's current base: \n \033[0m"))
    while base_from < 2 or base_from > 16:
        base_from = int(input("\033[33m the base was invalid (must be 1-16), please reinsert the base: \n \033[0m"))

    number_str = input("\033[32m input the NUMBER in its base form: \n \033[0m")
    while True:
        try:
            number = int(number_str, base_from)
            break
        except ValueError:
            number_str = input(
                f"\033[33m '{number_str}' isn't valid for base {base_from}, please reinsert the number: \n \033[0m"
            )

    base_to = int(input("\033[32m what base are u converting the number to: \n \033[0m"))
    while base_to < 2 or base_to > 16:
        base_to = int(input("\033[33m the base was invalid (must be 2-16), please reinsert the base: \n \033[0m"))

    print("\ngive me a sec...... \n")
    return number, base_from, base_to

def convertbase(number, base_from, base_to):

    if number == 0 :
        answer = '0'
        return answer
    
    if base_to == 10 :
        answer = [number, base_from]
        return str(answer[0])
    
    if base_to != 10 :
        digit_map = "0123456789abcdef"
        answer = None
        conv = []
        while number > 0 :
            conv.append(number % base_to)
            number = int(number / base_to)
        conv_answer = conv[::-1]
        answer = "".join(digit_map[nums] for nums in conv_answer)
    return answer

number_a, base_from_a, base_to_a = ask_input()

print(convertbase(number_a, base_from_a, base_to_a))
