import json
from pathlib import Path
from librarybookmanager import Book
import logging

# Logging setup
logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


class LibraryInventory:
    def _init_(self, data_file="data/books.json"):
        self.data_file = Path(data_file)
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            if self.data_file.exists():
                with open(self.data_file, "r") as f:
                    book_list = json.load(f)
                    self.books = [Book(**b) for b in book_list]
                    logging.info("Books loaded successfully.")
            else:
                self.data_file.parent.mkdir(exist_ok=True)
                self.data_file.write_text("[]")
        except Exception as e:
            logging.error(f"Error loading books: {e}")
            self.books = []

    def save_books(self):
        try:
            with open(self.data_file, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
            logging.info("Books saved successfully.")
        except Exception as e:
            logging.error(f"Error saving books: {e}")

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return [b for b in self.books if b.isbn == isbn]

    def display_all(self):
        return self.books