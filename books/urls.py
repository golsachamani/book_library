from django.urls import path
from . views import home, book_list,book_detail
urlpatterns = [
    
    path('', home, name = 'home'),
    path('books/', book_list, name='book_list'),
    path('book_detail/<int:pk>/', book_detail, name='book_detail'),
]
