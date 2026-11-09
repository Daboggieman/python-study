import json

# when the data to be loaded is ready and u want to export it to a json file, use this code snippet
data = {} # ready data to load into the file
with open("file_name.json", 'w') as whatever_u_want_to_call_it:
    json.dump(data, whatever_u_want_to_call_it, indent=4)


#aalso know that there is a difference between json.dump, and json.dumps, the first one is used to dump data into a json file, and the second one is used to dump data into a json string

# indent=4 is used to make the json file more readable, it adds 4 spaces of indentation to the json file, you can change the number to any number you want, or remove it if you don't want any indentation



# it is advicable to implement error handling when loading or dumping  data to or from a json file

try:
    with open("data.json", "w") as file:
        data = json.dump(data, file, indent=4)

except FileNotFoundError:
    print("The file does not exist.")

except json.JSONDecodeError:
    print("The JSON file contains invalid syntax.")

except PermissionError:
    print("You don't have permission to read this file.")

# if you want to handle multiple exceptions in a single except block, you can do it like this

try:
        # some code that lead exception
    pass

except (FileNotFoundError, PermissionError):
    print("Unable to access the file.")

# there are many more type of error to handle, but these are the most common ones, you can handle the erros as they occur, u dont need to have everything in place immediately