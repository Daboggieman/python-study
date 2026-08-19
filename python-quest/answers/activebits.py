# Write your solution here
def activebits():
    integer = int(input("Enter an integer: "))

    binary_representation = list(bin(integer)[2:])
    count = 0
    for bit in binary_representation:
        if bit == '1':
            count += 1
    print(f"The number of active 1 bits in the binary representation of {integer} is: {count}")
    return count

activebits()