# ------------------------------------------------------------
# Author: Shashi Kant
# Date: 19-Nov-2025
# Assignment 3 - Library Inventory System
# ------------------------------------------------------------

from library import Library
from book import Book
from member import Member

lib = Library()

print("\n===== Welcome to KR Mangalam Library System =====\n")

while True:
    print("""
    1. Add Book
    2. Register Member
    3. Borrow Book
    4. Return Book
    5. View Report
    6. Exit
    """)

    c = input("Enter your choice: ")

    if c == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        lib.add_book(Book(title, author, isbn))
        print("Book added.\n")

    elif c == "2":
        name = input("Member Name: ")
        mid = input("Member ID: ")
        lib.register_member(Member(name, mid))
        print("Member registered.\n")

    elif c == "3":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        print(lib.lend_book(mid, isbn))

    elif c == "4":
        mid = input("Member ID: ")
        isbn = input("Book ISBN: ")
        print(lib.take_return(mid, isbn))

    elif c == "5":
        lib.analytics_report()

    elif c == "6":
        lib.save_data()
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.\n")
