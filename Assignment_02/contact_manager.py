# Contact Manager - Unique Project Version
# Name: Shashi Kant
# Date: 17-11-2025
# Project: Smart Contact Book System (Enhanced & Unique)

import csv
import json
from datetime import datetime
import os

CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json"
LOG_FILE = "error_log.txt"

def log_error(operation, error):
    try:
        with open(LOG_FILE, "a") as log:
            log.write(
                f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] \n"
                f"Operation : {operation}\n"
                f"Error     : {str(error)}\n"
                f"-----------------------------\n"
            )
    except:
        pass


class SmartContactBook:

    def __init__(self):
        self.ensure_csv_exists()
        print("\n📘 Smart Contact Book Loaded Successfully!")

    def ensure_csv_exists(self):
        if not os.path.exists(CSV_FILE):
            with open(CSV_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Phone", "Email"])

    def add_contact(self):
        name = input("Enter Full Name       : ")
        phone = input("Enter Phone Number    : ")
        email = input("Enter Email Address   : ")

        try:
            with open(CSV_FILE, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([name, phone, email])
            print("\n✔ Contact Added Successfully!\n")
        except Exception as e:
            log_error("Add Contact", e)
            print("❌ Failed to save contact\n")

    def display_contacts(self):
        try:
            with open(CSV_FILE, "r") as file:
                rows = list(csv.reader(file))

            if len(rows) <= 1:
                print("⚠ No contacts available.\n")
                return

            print("\n📄 Saved Contacts:")
            print("=" * 55)
            print(f"{'Name':15} | {'Phone':15} | {'Email'}")
            print("-" * 55)

            for row in rows[1:]:
                print(f"{row[0]:15} | {row[1]:15} | {row[2]}")

            print("=" * 55 + "\n")

        except Exception as e:
            log_error("Display Contacts", e)
            print("❌ Cannot read contact file\n")

    def search_contact(self):
        name = input("Enter name to search: ").lower()
        try:
            with open(CSV_FILE, "r") as file:
                rows = list(csv.reader(file))

            for row in rows[1:]:
                if row[0].lower() == name:
                    print("\n✔ Contact Found:")
                    print(f"Name : {row[0]}")
                    print(f"Phone: {row[1]}")
                    print(f"Email: {row[2]}\n")
                    return

            print("❌ Contact not found!\n")

        except Exception as e:
            log_error("Search Contact", e)
            print("❌ Error while searching!\n")

    def update_contact(self):
        name = input("Enter name to update: ").lower()

        try:
            with open(CSV_FILE, "r") as file:
                rows = list(csv.reader(file))

            updated = False

            for row in rows[1:]:
                if row[0].lower() == name:
                    print("1. Update Phone")
                    print("2. Update Email")
                    ch = input("Enter choice: ")

                    if ch == "1":
                        row[1] = input("Enter new phone: ")
                    elif ch == "2":
                        row[2] = input("Enter new email: ")
                    else:
                        print("❌ Invalid choice!")
                        return

                    updated = True
                    break

            if updated:
                with open(CSV_FILE, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print("✔ Contact updated!\n")
            else:
                print("❌ Contact not found!\n")

        except Exception as e:
            log_error("Update Contact", e)
            print("❌ Update failed!\n")

    def delete_contact(self):
        name = input("Enter name to delete: ").lower()

        try:
            with open(CSV_FILE, "r") as file:
                rows = list(csv.reader(file))

            new_rows = [rows[0]]
            deleted = False

            for row in rows[1:]:
                if row[0].lower() != name:
                    new_rows.append(row)
                else:
                    deleted = True

            if deleted:
                with open(CSV_FILE, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerows(new_rows)
                print("✔ Contact deleted!\n")
            else:
                print("❌ Contact not found!\n")

        except Exception as e:
            log_error("Delete Contact", e)
            print("❌ Delete failed!\n")

    def export_json(self):
        try:
            with open(CSV_FILE, "r") as file:
                reader = csv.DictReader(file)
                contacts = list(reader)

            with open(JSON_FILE, "w") as jf:
                json.dump(contacts, jf, indent=4)

            print("✔ Exported to JSON!\n")
        except Exception as e:
            log_error("Export JSON", e)
            print("❌ JSON export failed!\n")

    def load_json(self):
        try:
            with open(JSON_FILE, "r") as jf:
                contacts = json.load(jf)

            print("\n📘 Contacts from JSON:")
            print("=" * 55)

            for c in contacts:
                print(f"{c['Name']:15} | {c['Phone']:15} | {c['Email']}")

            print("=" * 55 + "\n")

        except Exception as e:
            log_error("Load JSON", e)
            print("❌ Failed to load JSON!\n")


def main():
    obj = SmartContactBook()
    while True:
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Export to JSON")
        print("7. Load from JSON")
        print("8. Exit\n")

        ch = input("Enter choice: ")

        if ch == "1": obj.add_contact()
        elif ch == "2": obj.display_contacts()
        elif ch == "3": obj.search_contact()
        elif ch == "4": obj.update_contact()
        elif ch == "5": obj.delete_contact()
        elif ch == "6": obj.export_json()
        elif ch == "7": obj.load_json()
        elif ch == "8":
            print("Thank you for using Smart Contact Book!")
            break
        else:
            print("❌ Invalid choice!\n")


if __name__ == "__main__":
    main()
