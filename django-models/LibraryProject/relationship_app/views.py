from django.shortcuts import render
from .models import Book,Library
from django.views.generic import DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name="library"

def ListBooks(request):
    books=Book.objects.all()
    return render(request,'list_books.html',{'books':books})