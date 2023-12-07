class Book:
    # author
    # title
    # pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        # iii)
# A function that returns only the book title and it's author
    # A function that only returns the book title and its author
    def __str__(self):
        return f'{self.title}, {self.author}'
        
book_info = Book('Wells of Hope', 'B.Matthew', 178)
print(f'The book is called {book_info.title}, it was written by {book_info.author} and it has {book_info.pages} pages')

    
# ii)
class Ebook (Book):
    def __init__(self, title, author, pages, format):
        self.format =format
        super().__init__( title, author, pages)
ebook_info = Ebook('Wells of Hope', 'B.Matthew',178, 'pdf')
print (f'{ebook_info.title}, {ebook_info.author}, {ebook_info.pages}, {ebook_info.format}')
      
# iv)
# Class;Is like a function that is used to store attributes of an object or instance
# Object: Is a variable that has access to attributes of a class