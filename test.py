class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        print(book.title)
        print(book.author)
        self.keep = []
        for current_book in self.books:
            if (current_book.title != book) or (current_book.author != book):
                self.keep.append(current_book)
        self.book = self.keep   

    def search_books(self, search_string):
        matching_books = []
        for book in self.books:
                if (search_string in book.title) or (search_string in book.author):
                    matching_books.append(book)
        return matching_books
            




