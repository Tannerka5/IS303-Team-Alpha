# GROUP Hamburger Door Dash assingment
# Group 1

# THIS IS A GROUP ASSIGNMENT (USE GIT/GitHUB)
# Your task is to create a program that will help you familiarize yourself with various data structures available in the Python language.
import random
# You are the owner of a very successful hamburger restaurant. Your faithful customers line up every day and eat dozens of burgers. 
# You are writing a program to track exactly how many hamburgers each customer eats.

# Create an Order class
class Order():
    def __init__(self):
        self.burger_count = Order.randomBurgers(self)
# Create a constructor that defines an instance variable called burger_count
# Create a method called randomBurgers that returns a number between 1 and 20
    def randomBurgers(self):
        self.numBurgers = random.randrange(1,21)
        return self.numBurgers
# The constructor should call the randomBurgers() method and assign the return value to the burger_count instance variable
# Create a Person class
class Person():
    def __init__(self):
        self.customer_name = Person.randomName(self)
# Create a constructor that defines an instance variable called customer_name
# Create a method called randomName() that contains a list of 9 names:
#         asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return self.asCustomers([random.randrange(0,8)])

object = Person()
object.randomName()
print(Person.customer_name)


# This method randomly returns one of the 9 names when called
# The Person constructor should call the randomName() method and assign the return value (a random name) to the customer_name instance variable
class Customer(Person):
    def __init__(self, orderObject):
        super().__init__()
        self.order = orderObject
# Create a Customer class that inherits from the Person class
# Create a constructor that calls the parent constructor
# Create an instance variable called order in the constructor that is assigned an order object
# Create a variable for a Queue that will be assigned items of type Customer
queueOne = Customer()

# This variable will represent your line of customers (objects) waiting outside to place their hamburger orders

# Create a variable for a Dictionary with keys of type string and values of type int.
dictionaryOne = {
    "Jefe": 3,
    "El Guapo": 7, 
    "Lucky Day": 2,
    "Ned Nederlander": 5,
    "Dusty Bottoms": 9, 
    "Harry Flugleman": 3,
    "Carmen": 7, 
    "Invisible Swordsman": 2,
    "Singing Bush": 5,
}

# This variable will hold information about each customer
# Put 100 customers into the queue. Each customer object will already have a random number of burgers for each order
# Make sure there is a key in the dictionary for each customer before you try incrementing their total! Otherwise, add the customer to the dictionary.
# Print out each customer and their total burgers ordered sorted by the most number of burgers ordered
# NOTE: Remember that a queue in Python is a list data structure. Also, the randint() method from the random class returns a random number. For example:

# iRandomNum = random.randint(0,8)

# This returns a random integer between 0 and 8 (9 numbers).

# iRandomBurger = random.randint(1, 20)

# This would return a random number between 1 and 20.

# Sample Output
 

# Your sample output could look like:

 

# Table

# Description automatically generated

# You can use a statement similar to: listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True)

# NOTE: The listSortedCustomers is a new list variable, not a dictionary. Dictionaries cannot be sorted so this statement sorts the data from the dictionary 
# and stores it to a list. For each item in the list (representing a customer) there will be two positions 0 and

# 1. Position 0 contains the previous dictionaries key and position 1 contains the value.

# Now display the customer name and the total number of burgers consumed. Do this using a for loop displaying the contents of the list in positions 0 and 1.

# Make the customer name an even sized value using the ljust() function with the value of

# 19 as the parameter like customer[0].ljust(19) where customer is each list item object in the for loop.# Hamburger Door Dash Group Assignment

