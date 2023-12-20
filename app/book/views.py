from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, BookInstance, Author, Genre


def index(request):
    num_of_books = Book.objects.all().count()
    num_of_book_inst = Book.objects.count()
    available_book_inst = BookInstance.objects.filter(status__exact="a").count()
    num_of_authors = Author.objects.count()

    context = {
        "num_of_books": num_of_books,
        "num_of_book_inst": num_of_book_inst,
        "available_book_inst": available_book_inst,
        "num_of_authors": num_of_authors,
    }

    return render(request, "book/index.html", context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3


class BookDetailView(generic.DetailView):
    model = Book


class UserBooksListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = "book/borrowed_books.html"
    paginate_by = 3

    def get_queryset(self):
        return (
            BookInstance.objects.filter(borrower=self.request.user)
            .filter(status__exact="o")
            .order_by("due_back")
        )
