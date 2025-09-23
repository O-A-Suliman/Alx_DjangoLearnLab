from django.contrib import admin
from .models import Author,Book,Librarian,Library
admin.site.register([Author,Book,Librarian,Library])
# Register your models here.
