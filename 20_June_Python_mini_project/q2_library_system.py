# Aditya Kumar (20 June)

def add_book(catalog, book_id, title, author, year):
    if book_id not in catalog:
        catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print("Book borrowed:", catalog[book_id][0])
        else:
            print("Book already borrowed")
    else:
        print("Book not found")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned:", book_id)
    else:
        print("This book was not borrowed")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id in catalog:
        if book_id not in borrowed_books:
            title, author, year = catalog[book_id]
            print(book_id, "-", title, "by", author, "-", year)


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 1, "Python Basics", "Aditya Kumar", 2020)
    add_book(catalog, 2, "Machine Learning", "Rohit Sharma", 2021)
    add_book(catalog, 3, "Data Science", "Ayush Singh", 2022)
    add_book(catalog, 4, "Artificial Intelligence", "Tony Stark", 2023)

    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 101)
    register_member(members, 103)

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    return_book(borrowed_books, 1)

    print("\nMembers:", members)
    print("Borrowed Books:", borrowed_books)

    show_available(catalog, borrowed_books)


main()


# Dict is used for fast lookup of books by book_id.
# Tuple is used because book details should not change.
# List is used because borrowed books need insertion order.
# Set is used because member IDs must be unique.
