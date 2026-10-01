# def add(a, b)

# that returns the addition of two numbers.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b        

def subtract(a, b):
    return a - b        

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

print(add(2, 4)) # 6   
print(subtract(2, 4)) # -2
print(multiply(2, 4)) # 8
print(divide(2, 4))  # 0.5


# Create a function that determines whether a number is even or odd.


def even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(even_odd(2)) # Even
print(even_odd(3))  # Odd


# Create a function that returns the largest of three numbers without using max()

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest_of_three(1, 2, 3))  # 3
print(largest_of_three(3, 2, 1))  # 3


# Create a function that accepts a string and returns the number of vowels

vowels = "aeiou"

def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))  # 1


# Create a function that accepts a string and determines whether it is a palindrome

def Is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        return "Yes it is a palindrome"
    return "No it is not a palindrome"

print(Is_palindrome("racecar"))  # Yes it is a palindrome

print(Is_palindrome("hello"))  # No it is not a palindrome

# Create a function that accepts name, age, course and returns a formatted student profile. Use both positional and keyword arguments while calling it.

def create_profile(name, age, course):
    return f"Name: {name}, Age: {age}, Course: {course}"

# Using positional arguments
print(create_profile("Alice", 20, "Computer Science"))

# Using keyword arguments
print(create_profile(name="Bob", age=22, course="Mathematics"))



# Demonstrate the difference between a function that uses print() a function that uses return Explain through code why return is useful.
 
def print_function():
    print("This function uses print()")         

def return_function():
    return "This function uses return()"        

print_function()  # This will print the message but return None
result = return_function()  # This will return the message  
print(result)  # This will print the returned message           

#return is useful because it allows the function to send data back to the caller, which can be stored in a variable or used in further computations. In contrast, print() only outputs to the console and does not allow for further manipulation of the data.










