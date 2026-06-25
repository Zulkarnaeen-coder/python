class book :
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True
        print(f"The book {self.title} has been borrowed!")

    def return_book(self):
        self.__is_borrowed = False
        print(f"The book {self.title} has been returned!")

o1 = book("Jane Austen","Pride and Prejudice")
o2 = book("1984 ","Sheikh")
o3 = book("The Great Gatsby","Hasan")

for i in (o1,o2,o3):
     i.return_book()
     i.borrow