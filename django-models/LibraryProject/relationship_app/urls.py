from django.urls import path
from .views import LibraryDetailView
from .views import list_books

urlpatterns = [
    path("library_detail/",LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",list_books,name="list books"),
]
