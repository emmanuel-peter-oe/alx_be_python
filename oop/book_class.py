# book_class.py

class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize the Book instance.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor to indicate when a Book instance is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a user-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the Book.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
