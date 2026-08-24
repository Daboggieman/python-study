# from the directions in the python exercise folder, there are quite a few things to consider, add,
# logs should be savced in a json file.
# books should be given an id, use this medium to learn json file data arrangements and schematics
# action ON or WITH books should be subject to as many books as are involved, instead of assigning actions to books one by one.
# add a search system to it, and integrate some of the things u've learnt from DSA in here
import json
import os
import time

def json_inventory(filepath, action):
    if os.path.exists(filepath) and os.path.getsize(filepath):
        with open(filepath, "r") as actor:
            act = json.load(actor)
    else:
        act = []

    act.append(result)

    with open(filepath, "w") as actor:
        json.dump(act, actor, indent=2 )

def format_input(word): # this function still refuses to work when called, find if its problem is the code, its logic, or the way is being used/ called
    if word is str:
        if len(word) < 1:
            raise ValueError("invalid input")
        word.strip().lower()
    else:
        raise ValueError("invalid input / input type must be a string")
    return word

class Book:
    is_checked_out = False
    def __init__(self, title, author, isbn, location, rating):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.location = location
        self.rating = rating



class Library(Book):
        
    def __init__(self):
        pass
    
    def add_book(self, book, filepath):
        action = "add book"
        # if os.path(filepath).get(book.isbn) == book.isbn: # there is still some issue with this part, figure out the correct method to use
        new_book = {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "location": book.location,
            "is checked out": book.is_checked_out,
            "date Added": 0, # use the time import module to set the date and time of addition
        }
        # else:
        #     return "BOOK already exists in inventory"
        return new_book

    def checkout(self, book, given_to):
        book.is_checked_out = True
        action = "checkout"
        checkout_book = {
            "Action": action,
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "location": book.location,
            "is checked out": book.is_checked_out is True,
            "given to": f"{given_to}",
            "checkout date": 0, #use the time import module to set the date and time of checkout 
            "date Added": 0, # use the time import module to set the date and time of addition
        }
        return checkout_book
        

    def return_book(isbn):
        pass
    
    def list_available():
        pass

    def find_book(isbn):
        pass

    def remove_book(isbn):
        pass


book1 = Library()
inventory_path = "/home/student/python-study/OOP/solutions/json_output/library_inventory.json"
book_name = "engieneering mathematics volume 2"
result = book1.checkout(Book(f"{book_name}", "A.F Abott", "131", "isle 31, maths sections", "13+"), format_input(input(f"input the name of the person u are giving {book_name} to: \n")))
json_inventory(inventory_path, result)
print(result)

# list_available
# return_book(isbn)
# checkout(isbn)
# add_book(book)      - add other book details, probably through 'input'
