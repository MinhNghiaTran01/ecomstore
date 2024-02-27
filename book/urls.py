from django.urls import path
from .views import add_book
from .views import list_books
app_name = 'books'

urlpatterns = [
    # Các URL patterns khác của bạn ở đây
    path('add/', add_book, name='add_book'),
    path('list/', list_books, name='list_books'),
]
