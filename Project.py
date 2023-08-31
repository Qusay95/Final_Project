class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = True


class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    # TODO : implement member method
    def borrow_book(self, member_id, book_id):
        member = library.find_member(member_id)
        book = library.find_book(book_id)

        if member and book and book.is_available and member.level == book.level:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"   -- {self.name} has successfully borrowed {book.title}.")
        elif not book:
            print("   -- Book not found.")
        elif not member:
            print("   -- Member not found.")
        elif not book.is_available:
            print("   -- Book is not available.")
        else:
            print("   -- Member's level is not suitable for this book.")

    def return_book(self, member_id, book_id):
        member = library.find_member(member_id)
        book = library.find_book(book_id)

        if member and book in member.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"   -- {self.name} has successfully returned {book.title}.")
        elif not book:
            print("   -- Book not found.")
        elif not member:
            print("   -- Member not found.")
        else:
            print("   -- Member did not borrow this book.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
        pass

    def add_member(self, member):
        pass

    def display_books(self):
        pass

    def find_book(self, book_id):
        pass

    def display_members(self):
        pass

    def find_member(self, member_id):
        pass


library = Library()
print(' Welcome to the Library System '.center(100,'-'))
while True:
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice: ")

# TODO : implement the menu
