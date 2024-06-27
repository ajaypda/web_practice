from django.views.generic import ListView, DetailView
from .models import Library, Address

class LibraryListView(ListView):
    model = Library
    template_name = 'library_list.html'
    context_object_name = 'libraries'

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_list.html'
    context_object_name = 'library'

class AddressListView(ListView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'addresses'

class AddressDetailView(DetailView):
    model = Address
    template_name = 'address_list.html'
    context_object_name = 'address'
