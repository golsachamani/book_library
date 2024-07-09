from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from . models import *
from . forms import *
class BookListView(generic.ListView):
    models = Book
    queryset = Book.objects.order_by('author')
    templet_name ='lend/book_list.html'
    context_object_name = 'books'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'lend/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book =  self.get_object()
        comments = Comment.objects.filter(book=book)
        book_instance_count = BookInstace.objects.filter(book=self.object).count()
        book_instance_status = BookInstace.objects.filter(book=self.object).values('status')
        context['book_instance_count'] = book_instance_count
        context['book_instance_status'] = book_instance_status
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context
    @login_required
    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.member = request.member
            comment.save()
        return redirect('book-detail', pk=book.pk)

class LendBookView(generic.CreateView):
    model = Lend
    form_class =MemberForm
    template_name = 'lend/lend_book.html'

    def for_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
        return redirect('book_detail')