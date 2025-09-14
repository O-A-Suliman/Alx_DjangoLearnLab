import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author = Author.objects.get(name="John Doe")
    print("Books by John Doe:", author.books.all())

    # List all books in a library
    library = Library.objects.get(name="Central Library")
    print("Books in Central Library:", library.books.all())

    # Retrieve the librarian for a library
    print("Librarian of Central Library:", library.librarian.name)

if __name__ == "__main__":
    run_queries()
