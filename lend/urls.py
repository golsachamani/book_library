from django.urls import path,include
from .views import *
urlpatterns = [
   path('', BookListView.as_view(), name='book_list'),
   path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
   path('lendbook/',LendBookView.as_view(), name='lend_book'),
]
