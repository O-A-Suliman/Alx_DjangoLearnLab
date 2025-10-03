from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

urlpatterns = [
    path("library_detail/",views.LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",views.list_books,name="list books"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/',views.register, name='register'),
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),
]
