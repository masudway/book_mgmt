from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm

# Home view
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

# Add book view
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# Edit book view
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'add_book.html', {'form': form})

# Delete book view
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book:
        book.delete()
        return redirect('home')
    return render(request, 'delete_book.html', {'book': book})