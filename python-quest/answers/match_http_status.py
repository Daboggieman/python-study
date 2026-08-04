# Write your solution here
def describe_status(code):
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 404:
            return "Not Found"
        case 500:
            "Server Error"
        case _:
            return "Unknown"

print(describe_status(200))
print(describe_status(404))
print(describe_status(999))