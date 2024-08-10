from django.shortcuts import render
from . models import Book, Genre
def home(request):
    return render(request, 'books/home.html')

def book_list(request):
   books = Book.objects.all()
   return render(request, 'books/book_list.html', context ={'books':books})

def book_detail(request,pk):
    books = Book.objects.get(pk =pk)
    
    # title = books.title
    context = {'books':books}
    return render(request, 'books/book_detail.html', context = context)
    

