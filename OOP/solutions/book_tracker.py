# from the directions in the python exercise folder, there are quite a few things to consider, add,
# logs should be savced in a json file.
# books should be given an id, use this medium to learn json file data arrangements and schematics
# action ON or WITH books should be subject to as many books as are involved, instead of assigning actions to books one by one.
# add a search system to it, and integrate some of the things u've learnt from DSA in here


import json
import os
import tempfile
import time

def load_json(filepath):
    if os.path.exists(filepath) and os.path.getsize(filepath):
        try:
            with open(filepath, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            raise ValueError(f"Inventory log at {filepath} is corrupted")
    return []

def append_json_entry(filepath, entry):
    records = load_json(filepath)
    records.append(entry)

    directory = os.path.dirname(filepath) or "."
    fd, tmp_path = tempfile.mkstemp(dir=directory, suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as tmp_file:
            json.dump(records, tmp_file, indent=2)
        os.replace(tmp_path, filepath)
    except Exception:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise


def format_input(word):
    if not isinstance(word, str):
        raise ValueError("input type must be a string")
    word = word.strip().lower()
    if len(word) < 1:
        raise ValueError("invalid input")
    return word

class Book:
    def __init__(self, book_id, title, author, isbn, location, rating):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.location = location
        self.rating = rating
        self.is_checked_out = False
        self.given_to = None
        self.date_added = time.time()
        self.checkout_date = None

    def to_dict(self):
        return {
            "id": self.book_id,
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
            "location": self.location,
            "is_checked_out": self.is_checked_out,
            "given_to": self.given_to,
            "date_added": self.date_added,
            "checkout_date": self.checkout_date,
        }

    def __repr__(self):
        return f"Book({self.book_id}, {self.title!r}, isbn={self.isbn!r})"

class Library:
    def __init__(self, filepath):
        self.filepath = filepath
        self.books = {}
        self._isbn_index = {}
        self._next_id = 1

    def _log_action(self, action, book, extra=None):
        entry = {"action": action, **book.to_dict()}
        if extra:
            entry.update(extra)
        append_json_entry(self.filepath, entry)
        return entry

    def add_book(self, title, author, isbn, location, rating):
        if isbn in self._isbn_index:
            raise ValueError(f"Book with isbn {isbn} already exists")

        book = Book(self._next_id, title, author, isbn, location, rating)
        self.books[book.book_id] = book
        self._isbn_index[isbn] = book.book_id
        self._next_id += 1

        return self._log_action("add_book", book)

    def checkout(self, book_ids, given_to):
        if isinstance(book_ids, (str, int)):
            book_ids = [book_ids]

        results = []
        for book_id in book_ids:
            book = self.books.get(book_id)
            if book is None:
                raise ValueError(f"No book with id {book_id}")
            if book.is_checked_out:
                raise ValueError(f"'{book.title}' is already checked out")

            book.is_checked_out = True
            book.given_to = given_to
            book.checkout_date = time.time()
            results.append(self._log_action("checkout", book))

        return results

    def return_book(self, book_ids):
        if isinstance(book_ids, (str, int)):
            book_ids = [book_ids]

        results = []
        for book_id in book_ids:
            book = self.books.get(book_id)
            if book is None:
                raise ValueError(f"No book with id {book_id}")
            if not book.is_checked_out:
                raise ValueError(f"'{book.title}' was not checked out")

            book.is_checked_out = False
            book.given_to = None
            book.checkout_date = None
            results.append(self._log_action("return_book", book))

        return results

    def remove_book(self, book_id):
        book = self.books.pop(book_id, None)
        if book is None:
            raise ValueError(f"No book with id {book_id}")
        del self._isbn_index[book.isbn]
        return self._log_action("remove_book", book)

    def find_book(self, book_id):
        return self.books.get(book_id)

    def find_by_isbn(self, isbn):
        book_id = self._isbn_index.get(isbn)
        return self.books.get(book_id) if book_id is not None else None

    def list_available(self):
        return [b for b in self.books.values() if not b.is_checked_out]

    def search(self, query):
        query = format_input(query)
        return [
            b for b in self.books.values()
            if query in b.title.lower() or query in b.author.lower()
        ]



if __name__ == "__main__":
    inventory_path = os.path.join(os.path.dirname(__file__), "/home/student/python-study/OOP/solutions/json_output/library_inventory.json")
    library = Library(inventory_path)

    library.add_book("engineering mathematics volume 2", "A.F Abott", "131", "isle 31, maths section", "13+",)

    borrower = format_input(
        input("input the name of the person you are giving the book to: \n")
    )
    result = library.checkout(1, borrower)
    print(result)