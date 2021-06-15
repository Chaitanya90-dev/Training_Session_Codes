import os

class BMS:
    # this is used to store four modules : display,issue,return,add books

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"
        self.library_name = library_name
        self.book_dict = {}
        Id = 101 
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.book_dict.update({str(Id):{"books_title":line.replace("\n",""),"Status":"Avaliable"}})
            # print(self.book_dict)
            Id = Id + 1
            # print(line)

    def display_books(self):
        print("---------------- List of Books-----------------")
        print("Books ID", "\t", "Title")
        print("-----------------------------------------------")
        for key,value in self.book_dict.items():
            print(key, "\t\t", value.get('books_title'), "- [",value.get("Status"),"]")


    def issue_books(self):
        book_id = input("Enter Book ID to isuse book: ")
        if book_id in self.book_dict.keys():

            if not self.book_dict[book_id]["Status"] == "Avaliable":
                print("Sorry! This Book is Already Issue to Someone")
                return self.issue_books()

            elif self.book_dict[book_id]["Status"] == "Avaliable":
                self.book_dict[book_id]["Status"] = "Already Issued!"
                print("Book is issued Successfully. I hope this books will help you! \n")

            else:
                print("Book is Not Avalible in Library right now! \n We will get back to you soon! \n Thanks for suggestion!")
                return self.issue_books()

    def search_books(self):
        book_id = input("Enter Book ID to Search book: ")
        if book_id in self.book_dict.keys():
            if self.book_dict[book_id]["Status"] == "Avaliable":
                print("Book is Avaliable")
                return self.search_books()

        else: 
            print("Book ID not Found")
    
    def add_books(self):
        
        new_book = input("Enter New Book Title: ")
        if new_book == "":
            return self.add_books()

        elif len(new_book) > 30:
            print("Book Title is Too Much Long!\n Maximum 30 and Minimum 1 Aplhabets required")
            return self.add_books()

        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_book}\n")
                self.book_dict.update({str(int(max(self.book_dict))+1):{'books_title':new_book,'Status':'Avaliable'}})
                print(f"This book '{new_book}' has been added successfully!")

    def return_books(self):
        books_id = input("Enter a Book ID: ")
        if books_id in self.book_dict.keys():
            if self.book_dict[books_id]["Status"] == "Avaliable":
                print("This Books is already avaliable in library. So please check your book id")
                return self.return_books()

            elif not self.book_dict[books_id]["Status"] == "Avaliable":
                self.book_dict[books_id]["Status"] = ""
                self.book_dict[books_id]["Status"] = "Avaliable"
                print("Successfullt Returned Book")

        else:
            print("Book ID is not Found")


try: 
    myBMS = BMS("list_of_books.txt","Everyone's")
    press_key = {"D":"Display Books" , "I":"Issue Books", "S":"Search Books" , "A":"Add Books", "R":"Return Books", "Q":"Quit Books"}
    key_press = False
    while not(key_press == "q"):
        print(f"---------------------------Welcome to {myBMS.library_name} Library ----------------------------- \n")
        for key,value in press_key.items():
            print("Press", key , "To", value)
        key_press = input("Press Key: ").lower()
        if key_press == "i":
            print("Your Current Selection : Issue Books")
            myBMS.issue_books()

        elif key_press == "a":
            print("Your Current Selection : Add Books")
            myBMS.add_books()

        elif key_press == "s":
            print("Your Current Selcction : Search Books")
            myBMS.search_books()

        elif key_press == "d":
            print("Your Current Selection : Display Books")
            myBMS.display_books()

        elif key_press == "r":
            print("Your Current Selection : Return Books")
            myBMS.return_books()

        elif key_press == "q":
            print("Your Current Selection : Quit From Menu")
            break   
        else:
            continue

except Exception as e:
    print("Something went wrong",e)       


