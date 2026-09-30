# Create a function using *args that accepts any number of values and returns their total

from numpy import divide, divide, subtract


from numpy import subtract


def total(*args):
    return sum(args)

print(total(23, 4, 3))

#args -> collects any number of positional arguments into a tuple


# Create a function using *args that returns the largest supplied number.

def largest(*args):
    return max(args)

print(largest(23, 54, 67, 43, 12, 65))



# def create_profile(**kwargs)

# that accepts dynamic user information and prints all provided attributes.

def create_profile(**kwargs):
    return kwargs

print(create_profile(**{"Name": "Adwitiya", "Age": "22"}))

print(create_profile(name = "Rishi", Age = 21))

# Create a function that accepts another function as an argument

def func(callback):
    return callback()

def anotherfn():
    return "Hello from anotherfn!"

print(func(anotherfn)) 


# calculate(add, 10, 20)

# calculate(multiply, 10, 20)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 2, 4))
print(calculate(multiply, 2, 4))


# Create a lambda function for calculating the square of a number

# lambda parameters: expression

sqr = lambda a: a**2
print(sqr(9))


# Use lambda with map() to square [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda n: n ** 2, numbers))

print(squared)  # [1, 4, 9, 16, 25, 36]

# Use lambda with filter() to extract even numbers

even_No = list(filter(lambda n: n % 2 == 0, numbers))

print(even_No)  # [2, 4, 6]


# Write a recursive function to calculate factorial

def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n-1)

print(factorial(5)) # 120

# Write a recursive function to calculate 1 + 2 + 3 + ... + n

def add_n(n):
    if n == 0:
        return 0
    else:
        return n + add_n(n-1)

print(add_n(10)) # 55


# Write a recursive function to generate the Fibonacci sequence or calculate the nth Fibonacci number

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:        
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  

    
print(fibonacci(6))


# Demonstrate local and global variable scope using a small program 

message = "Hello, I am a global scope!"

def scope():
    local_msg = f"Hello, I am local scope"
    print(local_msg) #only accessible within the function
    print(message) #accessible within the function

scope()

# print(local_msg) #will give error as local_msg is not accessible outside the function


# Create a mini calculator where each mathematical operation is implemented as a separate function and a main function controls the program

def Add(a, b):
    return a + b                

def Multiply(a, b):
    return a * b        

def Subtract(a, b): 
    return a - b

def Divide(a, b):       
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def Calculate(operation, a, b):
    return operation(a, b)        


print(Calculate(Add, 2, 4)) # 6
print(Calculate(Multiply, 2, 4)) # 8
print(Calculate(Subtract, 2, 4)) # -2
print(Calculate(Divide, 2, 4)) # 0.5        

