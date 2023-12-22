class Library():
    def __init__(self):
        self.No_of_books = 0 
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)
        self.No_of_books = len(self.books)
    
    def showInfo(self):
        print(f"the no of books is {self.No_of_books} and the books are ")

        for i in self.books:
            print(i)    

l1 = Library()
l1.addBook("hindi") 
l1.addBook("english")        
l1.addBook("marathi") 
l1.showInfo() 