from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.can_create, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('', views.list_books, name='book_list'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('register/', views.register, name='register'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
