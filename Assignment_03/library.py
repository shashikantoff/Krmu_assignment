# ------------------------------------------------------------
# Author: Shashi Kant
# Date: 19-Nov-2025
# Assignment 3 - Library Inventory System
# ------------------------------------------------------------

import json
from book import Book
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.issued_count = {}

        self.load_data()

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def find_member(self, member_id):
        return next((m for m in self.members if m.member_id == member_id), None)

    def lend_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return "Member or Book not found."

        if member.borrow_book(book):
            self.issued_count[isbn] = self.issued_count.get(isbn, 0) + 1
            return f"{book.title} issued to {member.name}."
        return "Book is not available."

    def take_return(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member or not book:
            return "Invalid member or book!"

        if member.return_book(book):
            return f"{book.title} returned successfully."
        return "Return failed."

    def save_data(self):
        try:
            with open("books.json", "w") as f1:
                json.dump([b.to_dict() for b in self.books], f1, indent=4)

            with open("members.json", "w") as f2:
                json.dump([m.to_dict() for m in self.members], f2, indent=4)

        except Exception as err:
            print("Error saving:", err)

    def load_data(self):
        try:
            with open("books.json", "r") as f1:
                self.books = [Book.from_dict(b) for b in json.load(f1)]
        except:
            self.books = []

        try:
            with open("members.json", "r") as f2:
                self.members = [Member.from_dict(m) for m in json.load(f2)]
        except:
            self.members = []

    def analytics_report(self):
        total_books = len(self.books)
        active_members = len([m for m in self.members if len(m.borrowed_books) > 0])
        borrowed_now = len([b for b in self.books if not b.available])

        most_borrowed = None
        if self.issued_count:
            most_borrowed = max(self.issued_count, key=self.issued_count.get)

        print("\n----- Library Report -----")
        print(f"Total Books: {total_books}")
        print(f"Active Members: {active_members}")
        print(f"Books Borrowed Now: {borrowed_now}")

        if most_borrowed:
            b = self.find_book(most_borrowed)
            print(f"Most Borrowed: {b.title}")
        else:
            print("Most Borrowed: No data yet.")
        print("---------------------------")
