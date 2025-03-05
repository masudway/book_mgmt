from django.urls import path
from .views import home, add_book, edit_book, delete_book

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:book_id>/', edit_book, name='edit_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]
