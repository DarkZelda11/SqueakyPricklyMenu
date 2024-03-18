class Book:
  def __init__(self, title, author):
      self.title = title
      self.author = author

class Library:
  def __init__(self, books):
      self.books = books

# Aggregating Book instances to create a Library
book1 = Book("A Great Book", "Some Author")
book2 = Book("A Fantisy Novel", "The Fantisy Author")
book3 = Book("Life of a Book", "We love Books")

books_in_library = [book1, book2, book3]
my_library = Library(books_in_library)

# Accessing books in the library
for book in my_library.books:
  print(f"Title: {book.title}, Author: {book.author}")
