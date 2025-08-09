"""Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books."""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
    
    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
    
        