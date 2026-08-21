# let's attempt to manually convert - from base 10 to base 2,

def base10toX(number, target_base):

    if number == 0:
        return 0

    check_negative = number < 0

    absNumber = abs(number)
    if absNumber == 0:
        return 0

    remainder = []

    while absNumber > 0:
        if absNumber > 1:
            remainder.append(absNumber % target_base)
            absNumber = absNumber//target_base
        elif absNumber == 1:
            remainder.append(1)
            absNumber = 0
        else:
            absNumber = 0
    
    rems_map = {}
    for i in range(target_base):
        if i < 10:
            rems_map[i] = str(i)
        else:
            rems_map[i] = chr(65 + i - 10)
        
    mapped_remainder = []
    for r in remainder:
        mapped_remainder.append(rems_map[r])

    if check_negative:
        mapped_remainder.append("-")
    
    reversed_remainder = mapped_remainder[::-1]
    RevRems_to_string = ""
    
    for rems in reversed_remainder:
        RevRems_to_string += str(rems)
    return RevRems_to_string

def baseXto10(number , initial_base):

    if number == 0:
        return 0

    list_characters = []
    
    for char in number:
        list_characters.append(char)
    
    check_negative = False
    i = 0
    while i < len(list_characters):
        if list_characters[i] == "-":
            check_negative = True
            del list_characters[i]
        i += 1
    # for chars in list_characters:
    #     if chars == "-":
    #         check_negative = True
    #         list_characters = list_characters[1:]
    
    digit_map = {}
    for i in range(initial_base):
        if i < 10:
            digit_map[str(i)] = i
        else:
            digit_map[chr(65 + i - 10)] = i

    list_char_to_ints = []
    for char in list_characters:
        list_char_to_ints.append(digit_map[char])

    result = 0
    j = 0
    while j < len(list_char_to_ints):
        conv = list_char_to_ints[j] * (initial_base ** ((len(list_char_to_ints)-j)-1))
        result += conv
        j += 1
    
    if check_negative:
        result = result * -1

    return result

    
def baseXtoY(initial_base, number, target_base):

#to achieve the conversion from any base to another base, we could use the base x to 10 and base 10 to x functions
#first u convert the number from its initial base to base 10, then u convert the base 10 int to the target base

    init_base = initial_base
    orig_number = number
    targ_base = target_base

    origNumber_to_str = str(orig_number)

    if number == 0:
        return 0
    
    if initial_base == 10:
        return base10toX(orig_number, targ_base)
    if target_base == 10:
        return baseXto10(origNumber_to_str, init_base)

    initBase_to_base10 = baseXto10(origNumber_to_str, init_base)

    base10_to_targBse = base10toX(initBase_to_base10, targ_base)

    return base10_to_targBse

    # strNumber = str(number)
    # numberList = []

    # for nums in strNumber:
    #     numberList.append(int(nums))
    
    # for digits in numberList:
    #     pass

#


number_a = 406
initial_base_a = 7
target_base_a = 16

# print(base10toX(number_a, target_base_a))
# print(baseXto10(number_a, initial_base_a))
print(baseXtoY(initial_base_a, number_a, target_base_a))


