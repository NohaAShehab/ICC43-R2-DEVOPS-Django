from django.urls import path
from books.views import booksIndex, BookDetails, CreateBookView,EditBookView, DeleteBookView
urlpatterns = [
    path('index',booksIndex ),
    path('<int:pk>',BookDetails.as_view(), name='books.show'),
    path('create', CreateBookView.as_view()),
    path('edit/<int:pk>',EditBookView.as_view(), name='books.edit'),
    path('delete/<int:pk>',DeleteBookView.as_view(), name='books.delete'),
]
