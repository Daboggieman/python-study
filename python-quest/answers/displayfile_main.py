# Write your solution here
import sys

# def main() :
#     filename = sys.argv[1]
#     with open(filename, 'r') as content :
#         print(content.read())

# main('basicjoin.py')
#-------------------------------------------------------------------------------------
#
#
#EVERYTHING ABOVE IS ALREADY THE CORRECT ANSWER, ANYTHING BELOW IS JUST ME THINKERING
#
#
#-------------------------------------------------------------------------------------


##if the file argument is more than one then itll be handles as such

def main() :
    for filename in sys.argv[1:] :
        with open(filename, 'r') as content :
           print(f"\033[32m \n {content.name}\033[0m")
           print(f"{content.read()}\n")

if __name__ == "__main__":
    main()