from django.urls import path
from .views import LibraryDetailView
from.views import List_Books

urlpatterns = [
    path("library_detail/",LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",List_Books,name="list books"),
]
