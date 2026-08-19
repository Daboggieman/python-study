# Write your solution here
import sys

def main():
    if len(sys.argv) != 4 :
        print("arguments to 'doop' are not complete")
        print("if u used the multiplication(*) operator, \nplease be sure to insert it in a or double quote as thus '*' ")
        return
    first_int = int(sys.argv[1])
    second_int = int(sys.argv[3])
    operator = sys.argv[2]

    match operator :
        case "+" :
            result = first_int + second_int
        case "-" :
            result = first_int - second_int
        case "/" :
            result = first_int / second_int
        case "*" :
            result = first_int * second_int
        case "%" :
            result = first_int % second_int
        case "//" :
            result = first_int // second_int
        case _:
            print("unknown operator")
            return "Error"
    print(result)

if __name__ == "__main__":
    main()
