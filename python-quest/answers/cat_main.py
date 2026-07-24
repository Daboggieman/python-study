# Write your solution here
import sys

def main():
    if len(sys.argv) < 2:
        print("needs two files")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                print(f"--- {filename} ---")
                print(f.read())
        except FileNotFoundError:
            print(f"Error: '{filename}' not found.")
        except IOError as e:
            print(f"Error reading '{filename}': {e}")

if __name__ == "__main__":
    main()