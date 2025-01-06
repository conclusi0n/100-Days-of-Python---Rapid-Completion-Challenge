#Functions with Outputs
def add(a,b):
    return a+b
result =add(5,10)
print (result)

#Multiple Return Values
def get_coordinates():
    return 12.5, 16.3

x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # Output: x: 12.5, y: 16.3

#Docstrings
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

print(multiply.__doc__)  # Output: Returns the product of two numbers.

#Combining Dictionaries and Functions
def add_score(scores, student, score):
    """Adds a score for a student to the scores dictionary."""
    scores[student] = score
    return scores

student_scores = {}
student_scores = add_score(student_scores, "Alice", 95)
print(student_scores)  # Output: {'Alice': 95}

# While Loops, Flags, and Recursion
keep_running = True
while keep_running:
    user_input = input("Type 'stop' to quit: ")
    if user_input == "stop":
        keep_running = False

#Recursion
def factorial(n):
    """Calculates the factorial of a number using recursion."""
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


print("///////////////////////////////////////////////////////////")

# A simple calculator with functions, outputs, and a loop
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers."""
    if b != 0:
        return a / b
    return "Error! Division by zero."

# Main program loop
while True:
    print("\nSimple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    operation = input("Choose an operation (+, -, *, /): ")
    
    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation!"

    print(f"Result: {result}")
    
    # Ask if the user wants to continue
    if input("Do you want to continue? Type 'no' to exit: ").lower() == "no":
        print("Goodbye!")
        break
