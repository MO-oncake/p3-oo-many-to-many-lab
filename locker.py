class Author:
    def __init__(self, name = ""):
        self.name = name
        


class Book:
    def __init__(self, title = ""):
        self.title = title


class Contract:
    def __init__(self, Author, Book, date = "", royalties = int):
        self.author = Author
        self.book = Book
        self.date = date
        self.royalty = royalties
        