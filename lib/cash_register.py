#!/usr/bin/env python3
import ipdb

class CashRegister:
    # My attempt after the review
    pass
    def __init__(self, discount=0):
        pass
        self.discount = discount
        self.total = 0
        self.items = []
        self.prev_transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += (price * quantity)

        for i in range(quantity):
          self.items.append(title)

        self.prev_transactions.append({
           "title": title,
           "price": price,
           "quantity": quantity
        })

    def apply_discount(self):
        if self.discount > 0:
          self.total = self.total * ((100 - self.discount)/100)
          print(f"After the discount, the total comes to ${int(self.total)}.")
        else: 
            print("There is no discount to apply.")

    def void_last_transaction(self):
      self.total -= (self.prev_transactions[-1]["price"] * self.prev_transactions[-1]["quantity"])
      
      for i in range(self.prev_transactions[-1]["quantity"]):
        self.items.pop()
      
      if len(self.items) == 0:
         self.total = 0.0
      
      self.prev_transactions.pop()

# cr = CashRegister()
# ipdb.set_trace()

# My attempt prior to the review lecture
  # def __init__(self, discount=0):
  #   self.discount = discount
  #   self.total = 0
  #   self.items = []
  #   self.previous_transaction = {}
  
  # def add_item(self, title, price, quantity=1):
  #   self.total += price * quantity

  #   ran = range(quantity)
  #   for i in ran:
  #       self.items.append(title)

  #   self.previous_transaction = {
  #     "price": price,
  #     "title": title,
  #     "quantity": quantity
  #   }
    
  #   return self.items

  # def apply_discount(self):
  #   if self.discount:
  #     self.total = int(self.total - ( self.total * (self.discount/100)))
  #     print(f"After the discount, the total comes to ${self.total}.")
  #   else:
  #     print("There is no discount to apply.")
  
  # def void_last_transaction(self):
  #   pass
  #   for i in range(self.previous_transaction["quantity"]):
  #     self.items.pop()

  #   if len(self.items) == 0:
  #     self.total = 0.0
  #   else:
  #     subract_price = self.previous_transaction["quantity"] * self.previous_transaction["price"]
  #     self.total -= subract_price