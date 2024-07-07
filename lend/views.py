from django.shortcuts import render
from django.views import generic
from . models import *

class BookListView(generic.ListView):
    models = Book
    queryset = Book.objects.order_by('author')
    templet_name ='lend/book_list.html'
    context_object_name = 'books'

# class BookDetailView(generic.DetailView):

