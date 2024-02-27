
# Create your views here.
from django.shortcuts import render, redirect
from .form import BookForm
from .models import Book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list_books')
        else:
            print(form.errors)
      # Thay 'books:list_books' bằng URL của trang danh sách sách của bạn
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

def list_books(request):
    books = Book.objects.all()  # Lấy tất cả sách từ cơ sở dữ liệu
    return render(request, 'books/list_books.html', {'books': books})