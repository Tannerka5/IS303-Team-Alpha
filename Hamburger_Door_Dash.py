# Hamburger Door Dash Group Assignment
# Group 1
# Andrew Goldston, Andrew Matthews, Jordan Smith, Mitch Brammer, Tanner Atkinson, Zack Edgerton

import random

# Creating Order class
class Order:
    def __init__(self):
        self.burgerCount = Order.random_burgers(self)
    def random_burgers(self):
        self.numBurgers = random.randrange(1,21)
        return self.numBurgers

# Creating Person class
class Person:
    def __init__(self):
        self.customerName = Person.random_name(self)
    def random_name(self):
        self.asCustomers = [
            "Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", 
            "Dusty Bottoms", "Harry Flugleman", "Carmen", 
            "Invisible Swordsman", "Singing Bush"
            ]
        self.randomCustomer = random.choice(self.asCustomers)
        return self.randomCustomer

# Creating Customer inherited class
class Customer(Person):
    def __init__(self):
        super().__init__()
        self.order = Order()

# Defining queue and dictionary variables
queue = []
dict = {}

# Adding 100 customers queue and 
# increasing each customer's burger count with each addition
# and removing customers from the queue
for iCount in range(1,101):
    customer = Customer()
    queue.append(customer.customerName)
    if customer.customerName not in dict:
        dict[customer.customerName] = customer.order.burgerCount
    else:
        dict[customer.customerName] += customer.order.burgerCount
    queue.pop()

# Turn dictionary into a sorted list
listSortedCustomers = sorted(dict.items(), key=lambda x: x[1], reverse=True)

# Creating output
for x in range(0,9):
    currentCustomer = (listSortedCustomers [x][0]).ljust(25)
    print ((currentCustomer), (listSortedCustomers[x][1]))
