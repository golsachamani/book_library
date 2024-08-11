from django.urls import path
from . views import home, book_list,book_detail,author_detail,genre_detail
urlpatterns = [
    
    path('', home, name = 'home'),
    path('books/', book_list, name='book_list'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
    path('author_detail/<int:author_id>/', author_detail,name='author_detail'),
    path('genre_detail/<int:genre_id>/', genre_detail,name='genre_detail'),
]
