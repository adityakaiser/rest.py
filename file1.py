class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.__isborrowed=False
    def borrow(self):
        self.__isborrowed=True
        print("book has been successfully borrowed")
    def return_book(self):
        self.__isborrowed=False
        print("book has been successfully returned")
book1=book("Dragon ball","Akira Toriyama")
book2=book("one piece","Eichiro Oda")
book3=book("JoJo's Bizzare Adventure","Hirohiko Araki")
book1.borrow()
book1.return_book()
book2.borrow()
book2.return_book()
book3.borrow()
book3.return_book()