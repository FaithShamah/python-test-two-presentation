# #Loops
# #Basic: Write a Python program that prints all even numbers between 1 and 20 using a for loop.
# def even_numbers_btn_one_and_twenty():
#     for numbers in range(2,20,2):
#         print(numbers)
# even_numbers_btn_one_and_twenty()


# #Intermediate: Use a while loop to ask the user to input a number until they provide a number greater than 10.
def get_number_greater_than_ten():
    while True:
        number = int(input("Enter a number greater than 10: "))
        if number > 10:
            print("Yes! the number greater than 10.")
            break
        else:
            print("The number is not greater than 10. Try again.")

get_number_greater_than_ten()


# #Advanced: Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
# def multiplication_table():
#     # Outer loop for numbers 1 to 5
#     for i in range(1, 6):
#         print(f"Multiplication table for {i}:")
        
#         # Inner loop for numbers 1 to 10
#         for j in range(1, 11):
#             result = i * j
#             print(f"{i} x {j} = {result}")
#         print()  # Adds a blank line after each table for clarity

# multiplication_table()

# #Challenge: Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
# def sum_of_odd_numbers():
#     numbers = [4, 7, 2, 9, 12, 15]
#     total = 0
    
#     # Loop through each number in the list
#     for number in numbers:
#         if number % 2 != 0:  # Check if the number is odd
#             total += number   # Add the odd number to the total
    
#     print("The sum of odd numbers is:", total)

# sum_of_odd_numbers()






# # Lists
# # Basic: Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits=['Apple','Mango','Grapes','Strawberry','Orange']
for fruit in fruits:
    print(fruit)

# # # Intermediate: Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def square_numbers(numbers):
    squared_list = [num ** 2 for num in numbers]
    return squared_list
result = square_numbers([1,2,3])
print(result)

# # Advanced: Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# A combined  list.
combined = [item for pair in zip(list1, list2) for item in pair]
print(combined)

# Challenge: Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.
numbers = [3, 1, 4, 1, 5, 9, 2]
largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest 
        largest = num  
    elif num > second_largest:
        second_largest = num  
print(f"The two largest numbers are: {largest} and {second_largest}")




# # Dictionaries
# # Basic: Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.
# student ={'Name':'Jovia','Age':'21','Grade':'A'}
# print(student['Name'])
# print(student['Age'])
# print(student['Grade'])


# # Intermediate: Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
# def get_adults(people_dict):
#   adults = [name for name, age in people_dict.items() if age >= 21]
#   return adults
# people = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
# adult_names = get_adults(people)
# print(adult_names)


# # Advanced: Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.

# #Dictionary representing store items and their prices
# store_prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
# items_bought = ['apple', 'orange', 'banana', 'banana']
# total_cost = 0

# # for item in items_bought:
#     total_cost += store_prices.get(item, 0)  
# print("Total cost:", total_cost)



# # Challenge: Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
# # Given sentence
# sentence = "hello world hello"

# words = sentence.split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1  
#     else:
#         word_count[word] = 1  

# print(word_count)





# # Object-Oriented Programming (OOP)
# # Basic: Create a class called Car with attributes brand and color. Instantiate an object of the Car class and print its attributes.

# # Define the Car class
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand  
#         self.color = color  

# my_car = Car("Benz", "Black")

# print(f"Brand: {my_car.brand}")
# print(f"Color: {my_car.color}")

# # # Intermediate: Add a method called start_engine to the Car class that prints a message saying the engine of the car has started. Create an instance of Car and call the method.
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand  
#         self.color = color
#     def start_engine(self):
#         print(f"The engine of the {self.color} {self.brand} has started.")


# my_car = Car("Benz", "Black")
# my_car.start_engine()

# # Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
# # Deposit an amount.
# # Withdraw an amount (only if sufficient balance exists).
# # Print the account balance.
# class BankAccount:
#     def __init__(self,account_number,balance=0):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, amount):
#         # Deposit an amount into the account
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be greater than 0.")

#     def withdraw(self, amount):
#         # Withdraw an amount if sufficient balance exists
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
# #             print(f"Withdrew {amount}. New balance: {self.balance}")
# #         elif amount > self.balance:
# #             print("Insufficient balance for this withdrawal.")
# #         else:
#             print("Withdrawal amount must be greater than 0.")

#     def print_balance(self):
#         # Print the current balance of the account
#         print(f"Account balance: {self.balance}")


# # Create an instance of BankAccount
# my_account = BankAccount(account_number="123456789", balance=1000)

# # Deposit money
# my_account.deposit(500)

# # Withdraw money
# my_account.withdraw(300)

# # Print current balance
# my_account.print_balance()

# # Attempt to withdraw an amount greater than the balance
# my_account.withdraw(1500)


        
        
# Challenge: Implement a class called Library that manages a collection of books. Each book has a title, author, and available status. The Library class should have methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed).
class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"'{self.title}' by {self.author} ({'Available' if self.available else 'Not Available'})"

class Library:
    def __init__(self):
        self.books = []  # List to store the books in the library

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        """Remove a book from the library by title."""
        book_to_remove = next((book for book in self.books if book.title == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Removed: {book_to_remove}")
        else:
            print(f"Book '{title}' not found.")

    def check_availability(self, title):
        """Check if a book is available by title."""
        book = next((book for book in self.books if book.title == title), None)
        if book:
            return book.available
        return False

    def borrow_book(self, title):
        """Mark a book as unavailable if it's available."""
        book = next((book for book in self.books if book.title == title), None)
        if book and book.available:
            book.available = False
            print(f"You have borrowed '{book.title}'.")
        elif book:
            print(f"'{book.title}' is currently not available.")
        else:
            print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Mark a borrowed book as available."""
        book = next((book for book in self.books if book.title == title), None)
        if book and not book.available:
            book.available = True
            print(f"'{book.title}' has been returned and is now available.")
        elif book:
            print(f"'{book.title}' was not borrowed.")
        else:
            print(f"Book '{title}' not found in the library.")

    def list_books(self):
        """List all books in the library."""
        if self.books:
            print("Books in the library:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

# Example usage
library = Library()

# Add books to the library
library.add_book(Book("Maid In ManHattan", "John Legend"))
library.add_book(Book("2023", "Gerald Clitton"))
library.add_book(Book("The Great Sea", "Black CJ"))

# List all books in the library
library.list_books()

# Check availability of a book
print("Is '2023' available?", library.check_availability("2023"))

# Borrow a book
library.borrow_book("2023")

# Check availability after borrowing
print("Is '2023' available?", library.check_availability("2023"))

# Return the book
library.return_book("2023")

# List all books after returning
library.list_books()

# Remove a book
library.remove_book("The Great Sea by Black CJ ")

# List all books after removal
library.list_books()



        

