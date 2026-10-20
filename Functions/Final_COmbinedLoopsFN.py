# 1
# Student Result Management System

# Create functions to

# accept student marks

# calculate total

# calculate percentage

# assign grade

# determine pass/fail

# display result

# Use loops wherever appropriate.




# def accept_marks(number_of_subjects=5):
#     marks = []

#     for subject in range(number_of_subjects):
#         while True:
#             try:
#                 mark = float(input(f"Enter marks for subject {subject + 1} (0–100): "))
#                 if 0 <= mark <= 100:
#                     marks.append(mark)
#                     break
#                 print("Marks must be between 0 and 100.")
#             except ValueError:
#                 print("Please enter a valid number.")

#     return marks


# def calculate_total(marks):
#     return sum(marks)


# def calculate_percentage(marks):
#     return calculate_total(marks) / len(marks)


# def assign_grade(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage >= 40:
#         return "E"
#     else:
#         return "F"


# def determine_result(percentage):
#     return "Pass" if percentage >= 40 else "Fail"


# def display_result(marks):
#     total = calculate_total(marks)
#     percentage = calculate_percentage(marks)
#     grade = assign_grade(percentage)
#     result = determine_result(percentage)

#     print(f"Total: {total:.2f} / {len(marks) * 100}")
#     print(f"Percentage: {percentage:.2f}%")
#     print(f"Grade: {grade}")
#     print(f"Result: {result}")


# marks = accept_marks()
# display_result(marks)


# 2
# Banking Application

# Create a menu-driven banking program supporting

# Check balance

# Deposit

# Withdraw

# Transaction history

# Exit

# Use functions for each operation and while for the application menu.

# def banking_appln():
#     balance = 0
#     transaction_history = []

#     while True:
#             print("\nBanking Menu:")
#             print("1. Check Balance")
#             print("2. Deposit Money")
#             print("3. Withdraw Money")
#             print("4. Transaction History")
#             print("5. Exit")


#             choice = input("Enter a choice from 1-5: ")

#             if choice == '5':
#                 print("Exiting the banking application. Thank you!")
#                 break

#             if choice == "1":
#                 print(f"Balance is: {balance}")

#             elif choice == "2":
#                 user_deposit = float(input("Enter the money you want to deposit: "))
#                 if user_deposit > 0:
#                     balance += user_deposit
#                     print(f"Deposited money is: {user_deposit}, and Current balance is: {balance}")
#                     transaction_history.append(f"Deposited: {user_deposit}")
#                 else:
#                     print("Invalid deposit amount. Please enter a positive value.")

#             elif choice == "3":
#                 amount = float(input("Enter an amount to withdraw: "))
#                 if 0 < amount <= balance:
#                     balance -= amount
#                     print(f"Withdrawl amount is: {amount}, and current balance is: {balance}")
#                     transaction_history.append(f"Withdrawl: {amount}")
#                 else:
#                     print("Invalid amount. Please enter a positive value not exceeding your balance.")   

#             elif choice == "4":
#                 print("Transaction History:")
#                 if transaction_history:
#                     for transaction in transaction_history:
#                         print(transaction)
#                 else:
#                     print("No transactions yet.")

# banking_appln()
                




# 3
# Inventory Management

# Maintain products containing

# product name

# price

# quantity

# Provide functions to

# add product

# display products

# search product

# update quantity

# calculate total inventory value


# def inventory_management():
#     inventory = {}

#     def get_price():
#         while True:
#             try:
#                 price = float(input("Enter product price: "))
#                 if price < 0:
#                     print("Price cannot be negative.")
#                     continue
#                 return price
#             except ValueError:
#                 print("Invalid input. Enter a valid number.")

#     def get_quantity():
#         while True:
#             try:
#                 quantity = int(input("Enter product quantity: "))
#                 if quantity < 0:
#                     print("Quantity cannot be negative.")
#                     continue
#                 return quantity
#             except ValueError:
#                 print("Invalid input. Enter a whole number.")

#     def find_product(name):
#         for product_name in inventory:
#             if product_name.casefold() == name.casefold():
#                 return product_name
#         return None

#     def add_product():
#         name = input("Enter product name: ").strip()

#         if not name:
#             print("Product name cannot be empty.")
#             return

#         if find_product(name) is not None:
#             print("Product already exists. Use Update Quantity instead.")
#             return

#         price = get_price()
#         quantity = get_quantity()

#         inventory[name] = {
#             "price": price,
#             "quantity": quantity
#         }

#         print(f"Product '{name}' added successfully.")

#     def display_products():
#         if not inventory:
#             print("No products in inventory.")
#             return

#         print("\n--- Inventory ---")

#         for name, details in inventory.items():
#             print(
#                 f"Name: {name} | "
#                 f"Price: ₹{details['price']:.2f} | "
#                 f"Quantity: {details['quantity']}"
#             )

#     def search_product():
#         name = input("Enter product name to search: ").strip()
#         actual_name = find_product(name)

#         if actual_name is None:
#             print("Product not found.")
#             return

#         details = inventory[actual_name]
#         print(
#             f"Name: {actual_name} | "
#             f"Price: ₹{details['price']:.2f} | "
#             f"Quantity: {details['quantity']}"
#         )

#     def update_quantity():
#         name = input("Enter product name: ").strip()
#         actual_name = find_product(name)

#         if actual_name is None:
#             print("Product not found.")
#             return

#         new_quantity = get_quantity()
#         inventory[actual_name]["quantity"] = new_quantity

#         print(f"Quantity updated to {new_quantity}.")

#     def calculate_total_inventory_value():
#         total_value = sum(
#             details["price"] * details["quantity"]
#             for details in inventory.values()
#         )

#         print(f"Total Inventory Value: ₹{total_value:.2f}")

#     while True:
#         print("\n--- Inventory Management ---")
#         print("1. Add Product")
#         print("2. Display Products")
#         print("3. Search Product")
#         print("4. Update Quantity")
#         print("5. Calculate Total Inventory Value")
#         print("6. Exit")

#         choice = input("Choose an option (1-6): ").strip()

#         if choice == "1":
#             add_product()
#         elif choice == "2":
#             display_products()
#         elif choice == "3":
#             search_product()
#         elif choice == "4":
#             update_quantity()
#         elif choice == "5":
#             calculate_total_inventory_value()
#         elif choice == "6":
#             print("Exiting inventory management.")
#             break
#         else:
#             print("Invalid choice. Please select an option from 1 to 6.")


# if __name__ == "__main__":
#     inventory_management()




# 4
# Quiz Application

# Create at least 5 Python questions.

# The application should

# display one question at a time

# accept answers

# check answers

# maintain score

# show final percentage
def quiz_application():
    questions = [
        {"question": "What is the output of print(2 ** 3)?", "answer": "8"},
        {"question": "What is the keyword to define a function in Python?", "answer": "def"},
        {"question": "What data type is used to store text in Python?", "answer": "str"},
        {"question": "Which operator is used for floor division in Python?", "answer": "//"},
        {"question": "What is the output of print(len('Hello'))?", "answer": "5"}
    ]

    score = 0

    for i, q in enumerate(questions):
        user_answer = input(f"Q{i+1}: {q['question']} ")
        if user_answer.strip().lower() == q['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {q['answer']}")

    percentage = (score / len(questions)) * 100
    print(f"\nYour final score is: {score}/{len(questions)}")
    print(f"Your percentage is: {percentage:.2f}%")

if __name__ == "__main__":
    quiz_application()

# 5
# Number Analysis Tool

# Create a function that accepts a list and returns

# largest number

# smallest number

# total

# average

# even count

# odd count

# positive count

# negative count

# Do not use min(), max(), or sum().


# 5
# Number Analysis Tool

# Create a function that accepts a list and returns:
# largest number
# smallest number
# total
# average
# even count
# odd count
# positive count
# negative count

# Do not use min(), max(), or sum().

def number_analysis_tool(numbers):
    largest = None
    smallest = None
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for num in numbers:
        if largest is None or num > largest:
            largest = num

        if smallest is None or num < smallest:
            smallest = num

        total += num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    average = total / len(numbers) if numbers else 0

    return {
        "largest": largest,
        "smallest": smallest,
        "total": total,
        "average": average,
        "even_count": even_count,
        "odd_count": odd_count,
        "positive_count": positive_count,
        "negative_count": negative_count
    }


if __name__ == "__main__":
    numbers = []

    count = int(input("How many numbers do you want to enter? "))

    for i in range(count):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    analysis_result = number_analysis_tool(numbers)

    print("\nNumber Analysis Results:")
    for key, value in analysis_result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")



# 6
# Employee Salary Analyzer

# Given employee salaries, create functions to determine

# total payroll

# average salary

# highest salary

# lowest salary

# employees earning above average

# 6
# Employee Salary Analyzer

# Determine:
# total payroll
# average salary
# highest salary
# lowest salary
# employees earning above average

def employee_salary_analyzer(salaries):
    total_payroll = sum(salaries)

    average_salary = total_payroll / len(salaries) if salaries else 0

    highest_salary = max(salaries) if salaries else 0

    lowest_salary = min(salaries) if salaries else 0

    above_average_employees = [
        salary for salary in salaries
        if salary > average_salary
    ]

    return {
        "total_payroll": total_payroll,
        "average_salary": average_salary,
        "highest_salary": highest_salary,
        "lowest_salary": lowest_salary,
        "above_average_employees": above_average_employees
    }


if __name__ == "__main__":
    salaries = []

    count = int(input("Enter the number of employees: "))

    for i in range(count):
        salary = float(input(f"Enter salary of employee {i + 1}: "))
        salaries.append(salary)

    result = employee_salary_analyzer(salaries)

    print("\nEmployee Salary Analysis:")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


# 7
# Shopping Cart

# Create a simple cart where users can

# add products

# remove products

# view cart

# calculate bill

# exit

# The application should continue until Exit is selected.
def shopping_cart():    
    cart = []

    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the shopping cart. Thank you!")
            break
        elif choice == '1':
            product = input("Enter product name to add: ")
            cart.append(product)
            print(f"Product '{product}' added to cart.")
        elif choice == '2':
            product = input("Enter product name to remove: ")
            if product in cart:
                cart.remove(product)
                print(f"Product '{product}' removed from cart.")
            else:
                print(f"Product '{product}' not found in cart.")
        elif choice == '3':
            print("Current Cart:")
            if cart:
                for product in cart:
                    print(product)
            else:
                print("Cart is empty.")
        elif choice == '4':
            print(f"Total items in cart: {len(cart)}")
        else:
            print("Invalid choice. Please select a valid option.")

shopping_cart()

# 8
# Password Strength Checker

# Create a function that checks whether a password contains

# uppercase

# lowercase

# number

# special character

# minimum 8 characters

# Return a meaningful strength/result.

# 8
# Password Strength Checker

# Check whether a password contains:
# uppercase
# lowercase
# number
# special character
# minimum 8 characters

import re

def password_strength_checker(password):
    strength = "Weak"

    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)):

        strength = "Strong"

    return strength


if __name__ == "__main__":
    user_password = input("Enter your password: ")

    result = password_strength_checker(user_password)

    print(f"Password strength: {result}")


# 9
# Prime Number Analyzer

# Take two numbers representing a range.

# Create functions to

# find prime numbers

# count primes

# calculate their sum

# display the largest prime found

# Prime Number Analyzer


# 9
# Prime Number Analyzer

# Find prime numbers in a user-defined range.
# Count primes, calculate their sum, and find the largest prime.


def is_prime(check_number):
    if check_number <= 1:
        return False

    is_prime = True

    for i in range(2, check_number):
        if check_number % i == 0:
            is_prime = False
            break

    return is_prime


def prime_number_analyzer(start, end):
    primes = []

    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

    count = len(primes)
    total = sum(primes)
    largest = max(primes) if primes else None

    return {
        "primes": primes,
        "count": count,
        "total": total,
        "largest": largest
    }


if __name__ == "__main__":
    start_range = int(input("Enter the starting number: "))
    end_range = int(input("Enter the ending number: "))

    if start_range > end_range:
        print("Invalid range. Starting number must be <= ending number.")
    else:
        result = prime_number_analyzer(start_range, end_range)

        print(f"\nPrime Number Analysis ({start_range}-{end_range})")

        for key, value in result.items():
            print(f"{key.replace('_', ' ').title()}: {value}")



# 10
# Expense Tracker

# Allow a user to repeatedly enter

# expense name

# amount

# Provide options to

# add expense

# view expenses

# calculate total

# find highest expense

# exit

def expense_tracker():
    expenses = []

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Find Highest Expense")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '5':
            print("Exiting the expense tracker. Goodbye!")
            break
        elif choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter expense amount: "))
            expenses.append({"name": name, "amount": amount})
            print(f"Expense '{name}' added.")
        elif choice == '2':
            print("Current Expenses:")
            if expenses:
                for expense in expenses:
                    print(f"{expense['name']}: ${expense['amount']:.2f}")
            else:
                print("No expenses recorded.")
        elif choice == '3':
            total = sum(expense['amount'] for expense in expenses)
            print(f"Total expenses: ${total:.2f}")
        elif choice == '4':
            if expenses:
                highest = max(expenses, key=lambda x: x['amount'])
                print(f"Highest expense: {highest['name']} - ${highest['amount']:.2f}")
            else:
                print("No expenses recorded.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    expense_tracker()


# 11
# Mini Authentication System

# Create a small application supporting

# predefined username/password

# maximum login attempts

# successful login

# failed login

# logout

# retry logic

# Use functions and loops appropriately.

def mini_authentication_system():
    predefined_username = "admin"
    predefined_password = "password123"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == predefined_username and password == predefined_password:
            print("Login successful!")
            while True:
                action = input("Enter 'logout' to log out: ")
                if action.lower() == "logout":
                    print("Logged out successfully.")
                    return
        else:
            attempts += 1
            print(f"Login failed. Attempts remaining: {max_attempts - attempts}")

    print("Maximum login attempts reached. Access denied.")

if __name__ == "__main__":
    mini_authentication_system()

# 12
# Super30 Python Utility Application

# Create your own menu-driven application containing at least five utilities.

# Examples

# Calculator

# Palindrome checker

# Prime checker

# Factorial calculator

# Multiplication table

# Number analyzer

# Password checker

# Students are encouraged to add their own features


# 12
# Super30 Python Utility Application

def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


def palindrome_checker():
    text = input("Enter a word or phrase: ")
    cleaned = text.replace(" ", "").casefold()

    if cleaned == cleaned[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def prime_checker():
    num = int(input("Enter an integer: "))

    if num <= 1:
        print("Not a prime number.")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number.")
            return

    print("It is a prime number.")


def factorial_calculator():
    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined for negative integers.")
        return

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    print("Factorial:", factorial)


def multiplication_table():
    num = int(input("Enter a number: "))
    limit = int(input("Enter the table limit: "))

    if limit < 1:
        print("The limit must be at least 1.")
        return

    for i in range(1, limit + 1):
        print(f"{num} x {i} = {num * i}")


def number_analyzer():
    numbers_input = input(
        "Enter integers separated by spaces: "
    )

    try:
        numbers = [int(value) for value in numbers_input.split()]
    except ValueError:
        print("Invalid input. Enter integers only.")
        return

    if not numbers:
        print("Please enter at least one number.")
        return

    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for num in numbers:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

        total += num

        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Total:", total)
    print("Average:", total / len(numbers))
    print("Even count:", even_count)
    print("Odd count:", odd_count)
    print("Positive count:", positive_count)
    print("Negative count:", negative_count)


def password_checker():
    password = input("Enter a password: ")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(
        not char.isalnum() and not char.isspace()
        for char in password
    )

    if (len(password) >= 8 and has_upper
            and has_lower and has_digit and has_special):
        print("Password strength: Strong")
    else:
        print("Password strength: Weak")
        print("Requirements not met:")

        if len(password) < 8:
            print("- At least 8 characters")
        if not has_upper:
            print("- At least one uppercase letter")
        if not has_lower:
            print("- At least one lowercase letter")
        if not has_digit:
            print("- At least one digit")
        if not has_special:
            print("- At least one special character")


def super30_utility_application():
    while True:
        print("\n===== Super30 Python Utility Application =====")
        print("1. Calculator")
        print("2. Palindrome Checker")
        print("3. Prime Checker")
        print("4. Factorial Calculator")
        print("5. Multiplication Table")
        print("6. Number Analyzer")
        print("7. Password Checker")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            palindrome_checker()
        elif choice == "3":
            prime_checker()
        elif choice == "4":
            factorial_calculator()
        elif choice == "5":
            multiplication_table()
        elif choice == "6":
            number_analyzer()
        elif choice == "7":
            password_checker()
        elif choice == "8":
            print("Exiting the Super30 Utility Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 8.")


if __name__ == "__main__":
    super30_utility_application()
