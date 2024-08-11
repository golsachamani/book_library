from django.shortcuts import render,get_object_or_404
from . models import Book, Genre,Author
def home(request):
    return render(request, 'books/home.html')

def book_list(request):
   books = Book.objects.all()
   return render(request, 'books/book_list.html', context ={'books':books})

def book_detail(request,pk):
    # title, author = title_autor.split('/')
    book = Book.objects.get(pk=pk)
    
    context = {'book':book}
    return render(request,'books/book_detail.html', context = context)


def author_detail(request,author_id):
    author = Author.objects.get(pk = author_id)
    context = {'author':author}
    return render(request,'books/author_detail.html', context=context)
    

def genre_detail(request,genre_id):
    genre = Genre.objects.get(pk=genre_id)
    context = {'genre':genre}
    return render(request, 'books/genre_detail.html', context=context)