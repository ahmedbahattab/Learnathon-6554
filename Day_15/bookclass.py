'''Define a Python class called **`Book`** with the following requirements:

- The class should have attributes **`title`**, **`author`**, and **`published_year`**.
- Implement a constructor method that initializes these attributes.
- Implement a method called **`display_info()`** that prints out the book's information in a formatted manner.'''
class Book:
    def __init__(self, title, author, published_year):
        self.title = title
        self.author = author
        self.published_year = published_year

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Published Year:", self.published_year)

# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book1.display_info()
