# Write your solution here
import sys
import os
insert = sys.argv = list(input("\033[32minsert command line to check it's lenght: \n\033[0m"))

if len(insert) == 0:
    print("\033[31mError: EMPTY argumets passed\033[0m")
elif len(insert) % 2 == 0:
    print("even")
elif len(insert) % 2 != 0:
    print("odd")
else:
    print("\033[31minvalid arguments\033[0m")
    os.exit()