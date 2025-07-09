#!/usr/bin/env python3

# Define a Book class that models a book with a title and a page count
class Book:
    def __init__(self, title, page_count):
        # Initialize book attributes with title and page count
        self.title = title
        self.page_count = page_count  # This uses the property setter

    # Getter for page_count
    @property
    def page_count(self):
        return self._page_count

    # Setter for page_cunt with input validation
    @page_count.setter
    def page_count(self, value):
        # Ensure only integers are assigned
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Turn the page (via print)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
