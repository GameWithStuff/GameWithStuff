try:
    class Library:
        def __init__(this):
            print("Welcome to the Hogwards library of infinite books")
            this.borrowedBooks = set()
            try:
                with open("books.txt", "a") as f:
                    pass
            except:
                pass

        def noOfBorrowedBooks(this):
            return len(this.borrowedBooks)

        def add(self, name, doAdd=True):
            self.borrowedBooks.add(name)
            if doAdd:
                with open("books.txt", "a") as app:
                    app.write(f"{name}\n")

        def giveBack(self, name):
            self.borrowedBooks.remove(name)
            with open("books.txt", "w") as app:#*clears file
                pass
            with open("books.txt", "r") as read:
                while True:
                    line = read.readline()
                    if not line:
                        break
                    else:
                        if line == name:
                            pass
                        else:
                            with open("books.txt", "a") as app:
                                app.write(f"{name}\n")

    lib = Library()

    def loadBooks():
        with open("books.txt", "r") as read:
            while True:
                line = read.readline()
                if not line:
                    break
                else:
                    print("loading")
                    lib.add(line, False)

    loadBooks()

    while True:
        print("You have borrowed The following Books:")
        for i, book in enumerate(lib.borrowedBooks):
            print(f"{i+1}) {book}")
        print("\n")
        choice = "5"
        while not choice[0] in "1234":
            choice = input(
                "\nWhat Would you like to do?\n1) Borrow a book\n2) Return a Book\n3) Exit the Library\n4) Ask the librarian out on a date\n"
            )
        match choice:
            case "1":  #! borrow
                book = input("What book would you like to borrow:\n")
                if book in lib.borrowedBooks:
                    print(f"You have already borrowed {book}")
                else:
                    print(
                        "\nFrom whispers on the wind, a tale I now begin. With threads unseen, a book I weave within.\nInk of starlight, pages of mist, knowledge I request, with focused will, I insist.\nWords take form, stories unfold, wisdom unbound, be brave and bold."
                    )
                    print(f"Here is {book}")
                    lib.add(book)
            case "2":  #! Return
                book = input("What book would you like to return:\n")
                if book in lib.borrowedBooks:
                    print(
                        "Words unfurl, stories unwind, knowledge returned, peace I find.\nLavender's scent now fades away, the book I borrowed, I now repay.\nMoonlight fades, starlight dims, the tale is done, release the hymns"
                    )
                    print(f"Thanks for returning {book}")
                    lib.giveBack(book)
                else:
                    print("I can't accept that book we did not give it to you.")
            case "3":
                break
            case "4":
                print("I don't think you'd want to take a 70 year old out on a date.")
        print("\n\n\n\n\n")
except Exception as error:
    print(error)
    while True:
        pass
