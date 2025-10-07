from django.shortcuts import render, redirect, get_object_or_404
from .models import Library, Book
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login  
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.views.decorators.csrf import csrf_protect  
from .forms import BookForm 

# ==============================
# Role check helpers
# ==============================

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# ==============================
# Role-based views
# ==============================

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'bookshelf/member_view.html')

# ==============================
# User registration
# ==============================

@csrf_protect
def register(request):
    """
    Secure user registration view.
    Uses built-in UserCreationForm for automatic validation.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'bookshelf/register.html', {'form': form})

# ==============================
# Book views
# ==============================


def list_books(request):
    """
    Securely fetch all books using ORM (safe from SQL injection).
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "bookshelf/library_detail.html"
    context_object_name = "library"

# ==============================
# Secure CRUD operations
# ==============================

@csrf_protect
@permission_required('bookshelf.can_create', raise_exception=True)
def can_create(request):
    """
    Secure book creation with CSRF protection and form validation.
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/add_book.html", {"form": form})

@csrf_protect
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    Secure book editing using a ModelForm for input validation.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/edit_book.html", {"form": form, "book": book})

@csrf_protect
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    Secure book deletion with CSRF protection.
    """
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})
