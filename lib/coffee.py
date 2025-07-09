#!/usr/bin/env python3

# Define a Coffee class that models a coffee order with size and price
class Coffee:
    def __init__(self, size, price):
        # Initialize coffee attributes with size and price
        self.size = size  # Triggers the size setter
        self.price = price  # No validation needed for price

    # Getter for size
    @property
    def size(self):
        return self._size

    # Setter for size with validation against allowed options
    @size.setter
    def size(self, value):
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method to tip, with a print message
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1  # Increase the price by 1 to add a tip
