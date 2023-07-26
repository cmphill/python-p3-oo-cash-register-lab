#!/usr/bin/env python3

class CashRegister:
    def __init__(self, title="", discount=0, total=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.title = title
        self.item_prices = []  # Separate list to store individual item prices

    def add_item(self, title, price, quantity=1):
        for item in range(quantity):
            self.items.append(title)
            self.total += price
            self.item_prices.append(price)  # Store the price of each item in the list

    def apply_discount(self):
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        if self.discount != 0:
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            last_item_price = self.item_prices.pop()  # Remove the last item's price from the separate list
            self.total -= last_item_price 
