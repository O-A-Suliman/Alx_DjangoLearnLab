from .models import Author, Book
def get_author_by_name(author_name):
    return Author.objects.get(name=author_name)
def get_books_by_author(author):
    return Book.objects.filter(author=author)
