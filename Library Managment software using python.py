#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Gorisha bhawsar
#
# Created:     16/06/2023
# Copyright:   (c) Gorisha bhawsar 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Library():

    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks=len(self.books)

    def ShowInfo(self):
        print(f"The library has {self.noBooks} books,The Books are: ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("ikigai")
l1.addBook("Life's Amazing Secret")
l1.addBook("five point something")
l1.addBook("HC Verma")
l1.addBook("RS Agrawal")
l1.addBook("Harry Potter")
l1.addBook("S Chand")
l1.addBook("Game of Thrones")
l1.ShowInfo()



