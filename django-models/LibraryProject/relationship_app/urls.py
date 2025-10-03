from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

urlpatterns = [
    path("library_detail/",views.LibraryDetailView.as_view(),name="library detail"),
    path("list_books/",views.list_books,name="list books"),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/',views.register, name='register')
]
