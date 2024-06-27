from django.views.generic import ListView, DetailView
from .models import Book, Copy

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'book'

class CopyListView(ListView):
    model = Copy
    template_name = 'copy_list.html'
    context_object_name = 'copies'

class CopyDetailView(DetailView):
    model = Copy
    template_name = 'copy_list.html'
    context_object_name = 'copy'
