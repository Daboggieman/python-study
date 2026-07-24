# Write your solution here
import sys

def main():
    if len(sys.argv) < 2 :
        print("no string found, please insert string")
        return
    if len(sys.argv) > 2 :
        print("more than one string found, only one string is Required")
        return
    
    word = sys.argv[1]
    for char in word :
        if not char.isalpha() :
            # print(char)
            word = word.replace(char, "")
    title_word = word.title()
    return title_word
        
if __name__ == "__main__":
    print(main())