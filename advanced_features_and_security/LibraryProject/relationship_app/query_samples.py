# relationship_app/query_samples.py
from .models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "George Orwell"
author = Author.objects.get(name=author_name)   
books_by_author = Book.objects.filter(author=author)  
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"Books in {library_name}:")
for book in library.books.all():
    print(book.title)

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")
