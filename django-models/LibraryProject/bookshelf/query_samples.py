from .models import Author, Book, Library, Librarian

def get_author_by_name(author_name):
    return Author.objects.get(name=author_name)

def get_books_by_author(author):
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)
