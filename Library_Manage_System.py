class Library:
    def __init__(self,filename):
        self.filename=filename
        self.file=open(self.filename,"a+")
    def __del__(self):
        self.file.close()
    
    def list_book(self):
        self.file.seek(0)
        books=self.file.read().splitlines()
        book_num=0
        for book in books:
            book_num+=1
            book_info=book.split(',')
            if len(book_info)>=2:
                print(f"Book {book_num}:: {book_info[0]}, Author: {book_info[1]}")
    def add_book(self,title,author,year,page):
        self.file.write(f"\n{title},{author},{year},{page}")
        print("Book added successfully!!")
    def remove_book(self,title):
        with open('temp.txt',"w") as temp_file:
            self.file.seek(0)
            books=self.file.readlines()
            not_available=False
            for book in books:
                if title not in book:
                    temp_file.write(book)
                else:
                    not_available=True
        self.file.close()
        
        import os
        os.remove('books.txt')
        os.rename('temp.txt','books.txt')
        self.file=open('books.txt','a+')
        if not_available:
            print(f"Book '{title}' removed successfully!")
        else:
            print(f"Book '{title}' is not in the library.")
    
lib=Library("books.txt")
while True:
    print("***MENU***")
    print("1)List book")
    print("2)Add book")
    print("3)Remove book")
    print("q)Quit")
    choice=input("Enter your choice: ")
    
    if choice=='1':
        print("Listing books")
        lib.list_book()
    elif choice=='2':
        title=input("Title: ")
        author=input("Author: ")
        year=input("Year: ")
        page=input("Page: ")
        lib.add_book(title,author,year,page)
    elif choice=='3':
        b_name=input("Enter the title of the book to remove: ")
        lib.remove_book(b_name)
    elif choice == 'q':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")