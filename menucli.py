from librarybookmanager import Book
from libraryinventorymanager import LibraryInventory

def menu():
    inventory = LibraryInventory()

    while True:
        print("\n===== Library Inventory Manager =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            book = Book(title, author, isbn)
            inventory.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            books = inventory.search_by_isbn(isbn)
            if books:
                if books[0].issue():
                    inventory.save_books()
                    print("Book issued.")
                else:
                    print("Already issued.")
            else:
                print("Book not found.")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            books = inventory.search_by_isbn(isbn)
            if books:
                if books[0].return_book():
                    inventory.save_books()
                    print("Book returned.")
                else:
                    print("Already available.")
            else:
                print("Book not found.")

        elif choice == "4":
            all_books = inventory.display_all()
            for b in all_books:
                print(b)

        elif choice == "5":
            title = input("Enter title to search: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")