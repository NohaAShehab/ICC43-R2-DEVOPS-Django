from django.shortcuts import render
from books.forms import BookModelForm
# Create your views here.
from books.models import Book
from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def booksIndex(request):
    allbooks = Book.get_all_books()
    return render(request, "books/index.html", context={"books":allbooks})


class BookDetails(DetailView):
    model = Book
    template_name = "books/show.html"


class CreateBookView(CreateView):
    template_name = "books/create.html"
    form_class = BookModelForm
    success_url = '/books/index'

class EditBookView(UpdateView):
    template_name = "books/edit.html"
    form_class = BookModelForm
    success_url = '/books/index'
    model = Book



class DeleteBookView(DeleteView):
    template_name = "books/delete.html"
    model = Book
    success_url = '/books/index'