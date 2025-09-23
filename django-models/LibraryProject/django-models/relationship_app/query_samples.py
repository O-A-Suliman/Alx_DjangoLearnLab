import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "relationship_app.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "Author 1"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print("-", book.title)

library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)

library_name = "Central Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian of {library.name}: {librarian.name}")
