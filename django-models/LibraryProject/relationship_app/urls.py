from django.urls import path
from .views import LibraryDetailView
from .views import list_books
from .views import RegisterView
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

urlpatterns = [
    path("library_detail/",LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",list_books,name="list books"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/',RegisterView.as_view()),
]
