import json
import os

FILE = "library.json"


def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_book():
    data = load_data()
    book = {
        "id": input("Book ID: "),
        "title": input("Title: "),
        "author": input("Author: "),
        "available": True,
        "issued_to": None
    }
    data.append(book)
    save_data(data)
    print("✔ Book added successfully!")


def view_books():
    data = load_data()
    if not data:
        print("No books available.")
        return

    print("\n===== Library Books =====")
    for book in data:
        status = "Available" if book["available"] else f"Issued to {book['issued_to']}"
        print(f"{book['id']} - {book['title']} ({book['author']}) | {status}")


def issue_book():
    data = load_data()
    book_id = input("Enter Book ID to issue: ")

    for book in data:
        if book["id"] == book_id:
            if book["available"]:
                student = input("Enter student name: ")
                book["available"] = False
                book["issued_to"] = student
                save_data(data)
                print("📕 Book issued!")
                return
            else:
                print(f"❌ Already issued to {book['issued_to']}")
                return

    print("❌ Book ID not found!")


def return_book():
    data = load_data()
    book_id = input("Enter Book ID to return: ")

    for book in data:
        if book["id"] == book_id:
            if not book["available"]:
                book["available"] = True
                book["issued_to"] = None
                save_data(data)
                print("📗 Book returned!")
                return
            else:
                print("❌ This book was not issued.")
                return

    print("❌ Book ID not found!")


def menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1": add_book()
        elif choice == "2": view_books()
        elif choice == "3": issue_book()
        elif choice == "4": return_book()
        elif choice == "5": break
        else:
            print("Invalid choice!")

menu()
