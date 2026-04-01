# Real-life Mini Project

# Create a class Library with methods to:

# add a book

# remove a book

# display all books

# Ensure the library maintains a list of available books.


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Book '{book}' removed.")
        else:
            print("Book not found!")

    def display_books(self):
        if self.books:
            print("Books in Library:")
            # print("\n".join(f"- {b}" for b in self.books))
            for index,b in enumerate(self.books):
                print(index+1 ,".", b)
        else:
            print("No books available.")


# Example
lib = Library()
lib.add_book("Python Programming")
lib.add_book("Data Structures")
lib.display_books()
lib.remove_book("Data Structures")
lib.display_books()
