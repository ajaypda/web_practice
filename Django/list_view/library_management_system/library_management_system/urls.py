"""
URL configuration for library_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraries.views import LibraryListView, AddressListView, LibraryDetailView, AddressDetailView
from books.views import BookListView, CopyListView, BookDetailView, CopyDetailView
from members.views import MemberListView, MemberDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('libraries/', LibraryListView.as_view(), name='library-list'),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('copies/', CopyListView.as_view(), name='copy-list'),
    path('members/', MemberListView.as_view(), name='member-list'),

    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('copies/<int:pk>/', CopyDetailView.as_view(), name='copy-detail'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
]
