from django.urls import path
from .views import LibraryDetailView,ListBooks

urlpatterns = [
    path("library_detail/",LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",ListBooks,name="list books"),
]
