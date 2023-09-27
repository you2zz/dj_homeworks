from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    list_book = Book.objects.all()
    context = {'list_book': list_book}
    return render(request, template, context)

def books_pub_date(request, pub_date):
    template = 'books/books_pub_date.html'
    list_book_date = Book.objects.filter(pub_date=pub_date)
    list_book_date_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    if list_book_date_next:
        next_date = str(list_book_date_next.pub_date)
    else:
        next_date = None
    list_book_date_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').reverse().first()
    if list_book_date_previous:
        previous_date = str(list_book_date_previous.pub_date)
    else:
        previous_date = None

    context = {
        'list_book': list_book_date,
        'next_date': next_date,
        'previous_date': previous_date,
    }
    return render(request, template, context)