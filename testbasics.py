from librarybookmanager import Book

def test_book_issue():
    b = Book("Test", "Author", "123")
    assert b.issue() is True
    assert b.status == "issued"

def test_return():
    b = Book("Test", "Author", "123", "issued")
    assert b.return_book() is True
    assert b.status == "available"