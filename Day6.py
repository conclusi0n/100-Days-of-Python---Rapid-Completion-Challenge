#Defining and Calling Python Functions
def apple(fruits):                                                          #Defining a Function
    pass

def greet(name):
    print(f"Hello {name}")                                          #Calling a Function
greet("Biraj")

def add(a,b):
    return a+b

result = add(3,5)
print (result)                                      #With Return Values

def greet(name="User"):
    print(f"Hello, {name}!")

greet()            # Output: Hello, User!                   #Default Parameters:
greet("Biraj")     # Output: Hello, Biraj!

#Indentation in Python

def say_hello():
    print("Hello!")
    print("How are you?")

        #Nested Indentation
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

answer = check_even_odd(4)

#While Loops
apple = 0
while apple <= 10 :
    print(f"{apple} apple is red ")
    apple +=1
