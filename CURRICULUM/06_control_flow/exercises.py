# Exercise 06: Control Flow
# Run this script with: python exercises.py

# TODO: Exercise 1
# Given the score below, write an if-elif-else chain that prints:
# - "Excellent" if score is 90 or above.
# - "Good" if score is 70 to 89.
# - "Needs Improvement" if score is below 70.
score = 85
if score >= 90 and score <= 100 :
    print(f"score is {score}, EXCELLENT!" )
elif score < 90 and score >= 70 :
    print(f"score is {score}, GOOD!")
elif score < 70 and score >= 0:
    print(f"score is {score}, NEEDS IMPROVEMENT!")
else:
    print("invalid score, score must be between 0 to 100")


# TODO: Exercise 2
# Write a print statement using a ternary operator (one line) that prints "Can Vote"
# if the age variable is 18 or older, and "Cannot Vote" otherwise.
age = 20

can_vote = "can vote" if age > 17 else "cannot vote"
print(can_vote)


# TODO: Exercise 3
# Write a match-case statement for the variable 'role' below:
# - If role is "admin", print "Full access"
# - If role is "editor" or "author", print "Write access"
# - If role is "guest", print "Read access"
# - Otherwise, print "No access"
role = input("Are you an admin, editor, author, or guest? \n Enter your role: ")
match role:
    case "admin":
        print("full access")
    case "editor" | "author":
        print("write access")
    case "guest":
        print("read access")
    case _ :
        print("no access")


# TODO: Exercise 4
# Check if the list 'items' is empty or not using truthy/falsy check.
# Print "Empty list" or "Items present".
items = []

if items:
    print("Items present")
else:
    print("Empty list")