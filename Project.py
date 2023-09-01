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
    # I will put ( borrow_book & return_book ) in class Library


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        print(f"   -- ID\t|\t\tTitle\t\t|\t\tAuthor\t\t|\t\tLevel\t|\t\tAvailable")
        print('-' * 90)
        for book in self.books:
            print(f"   -- {book.book_id}\t\t|\t\t{book.title}\t\t|\t\t{book.author}\t\t|\t\t{book.level}\t\t|\t\t{'Yes' if book.is_available else 'No'}")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_members(self):
        print(f"   -- ID\t\t|\t\tName\t\t\t|\t\tEmail\t\t\t\t\t|\tLevel")
        print('-' * 90)
        for member in self.members:
            print(f"   -- {member.member_id}\t\t\t|\t\t{member.name}\t\t\t|\t\t{member.email}\t\t|\t\t{member.level}")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book and book.is_available and member.level == book.level:
            member.borrowed_books.append(book)
            book.is_available = False
            print(f"   -- {member.name} has successfully borrowed {book.title}.")
        elif not book:
            print("   -- Book not found.")
        elif not member:
            print("   -- Member not found.")
        elif not book.is_available:
            print("   -- Book is not available.")
        else:
            print("   -- Member's level is not suitable for this book.")

    def return_book(self, member_id, book_id):
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book in member.borrowed_books:
            member.borrowed_books.remove(book)
            book.is_available = True
            print(f"   -- {member.name} has successfully returned {book.title}.")
        elif not book:
            print("   -- Book not found.")
        elif not member:
            print("   -- Member not found.")
        else:
            print("   -- Member did not borrow this book.")

library = Library()
print(' Welcome to the Library System '.center(100, '-'))
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
    print(" ")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(" # Add Member")
        name = input(" * Enter member name : ")
        email = input(" * Enter member email : ")
        level = input(" * Enter member level : ")
        member = Member(name, email, level)
        library.add_member(member)
        print(" ")

    elif choice == 2:
        print(" # Edit Member")
        member_id = int(input(" * Enter Member ID: "))
        library.find_member(member_id)
        name = input(" * Enter member name : ")
        email = input(" * Enter member email : ")
        level = input(" * Enter member level : ")
        member = Member(name, email, level)
        library.members.pop(member_id-1)
        library.members.insert(member_id-1, member)
        print(" ")

    elif choice == 3:
        print(" # Show Members")
        library.display_members()
        print(" ")

    elif choice == 4:
        print(" # Delete Member")
        index = int(input(" * Enter Member ID: "))
        library.members.pop(index-1)
        print(f"   -- Member {index} is deleted ")
        print(" ")

    elif choice == 5:
        print(" # Add Book")
        title = input(" * Enter book title : ")
        author = input(" * Enter book author : ")
        level = input(" * Enter book level : ")
        book = Book(title, author, level)
        library.add_book(book)
        print(" ")

    elif choice == 6:
        print(" # Show Books")
        library.display_books()
        print(" ")

    elif choice == 7:
        print(" # Borrow Book")
        member_id = int(input(" * Enter Member ID: "))
        book_id = int(input(" * Enter Book ID: "))
        library.borrow_book(member_id, book_id)
        print(" ")

    elif choice == 8:
        print(" # Return Book")
        member_id = int(input(" * Enter Member ID: "))
        book_id = int(input(" * Enter Book ID: "))
        library.return_book(member_id, book_id)
        print(" ")

    elif choice == 9:
        print(" # Exit")
        print("   -- Thank you.. Goodbye")
        break

    else:
        print("   -- Invalid choice. Please put valid option.")
