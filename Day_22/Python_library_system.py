class LibraryItem:
    def display_info(self):
        pass  # Placeholder method to be overridden in subclasses

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)

class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def display_info(self):
        print("DVD Title:", self.title)
        print("Director:", self.director)
        print("Duration:", self.duration)

# Creating instances of Book and DVD
book = Book("Python Programming", "John Smith", "978-1-2345-6789-0")
dvd = DVD("The Matrix", "Lana Wachowski, Lilly Wachowski", "2 hours")

# Calling the display_info() method on each instance
print("Book Information:")
book.display_info()
print("\nDVD Information:")
dvd.display_info()
