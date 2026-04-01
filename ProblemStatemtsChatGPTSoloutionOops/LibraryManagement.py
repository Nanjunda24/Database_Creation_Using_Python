# Real-life Mini Project

# Create a class Library with methods to:

# add a book

# remove a book

# display all books

# Ensure the library maintains a list of available books

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"{book} addedd successfully!!! ") 

    def remove_book(self,book):
        self.books.remove(book)
        print(f"{book} remove successfully!!!!!")

    def display_books(self):
       
        if len(self.books) == 0:
            print("No books are available!!!")
        else:
            print("Number of books available in library: ",len(self.books))
            look = input("Want to see books which are all there in library yes/no:  ").lower()
            if look == "yes":
                print("Books in library: ")
                for book in self.books:
                    print(f"------>{book}")
            else:
                print("Thank you !!!!")


l = Library()

l.add_book("Java")
l.add_book("Python data structure")
l.add_book("Nanjunda")
l.remove_book("Nanjunda")
#l.remove_book("Java")
l#.remove_book("Python data structure")
l.display_books()
        
    