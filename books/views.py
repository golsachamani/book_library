from django.shortcuts import render,get_object_or_404
from . models import Book, Genre,Author,BookInstance
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

def book_borrow(request, author_title):
    author, title = author_title.split("/")
    book = Book.objects.filter(
        title__iexact=title, author__fullname__iexact=author
    ).get()

    due_time = datetime.now() + timedelta(days=10)
    user = request.user
    book.borrow(user, due_time)

    return redirect(reverse("book-detail", args=[author_title]))

def book_instance(request, id):
    book_instance = BookInstace.objects.get(pk=id)
    context = {
        "title": book_instance.book.title,
        "book_instance": book_instance,
    }
    return render(request=request, template_name="book-instance.html", context=context)


def author_detail(request,author_id):
    author = Author.objects.get(pk = author_id)
    context = {'author':author}
    return render(request,'books/author_detail.html', context=context)
    

def genre_detail(request,name):
    genre = Genre.objects.filter(name__iexact=name).get()
    context = {'genre':genre}
    return render(request, 'books/genre_detail.html', context=context)