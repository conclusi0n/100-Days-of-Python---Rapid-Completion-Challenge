#Python Primitive Data Types
hello_int= 100
hello_float= 192.168
hello_str = "Biraj"
hello_bool= True
print (type( hello_int))
print (type(hello_bool))
print (type(hello_float))
print (type(hello_str))
print ( hello_int)
print (hello_bool)
print (hello_float)
print (hello_str)
#Type Error, Type Checking and Type Conversion

#This line is an error     print("Hello world: " + 69)
print("Hello world: " + str(69))        #correct one 

#Type Checking

x="apple"
print (type(x))
y=100
print (type(y))


#Type Conversion

world_str="69"
world_int =int(world_str)

pi= 3.14
pi_str = str(pi)

#Mathematical Operations
a= 1
b= 2

print(a + b)   # Output: 13
print(a - b)   # Output: 7
print(a * b)   # Output: 30
print(a / b)   # Output: 3.3333...
print(a // b)  # Output: 3
print(a % b)   # Output: 1
print(a ** b)  # Output: 1000 (10^3)

#Number Manipulation and F-Strings

result=3.144545
print(round(result))
print(round(result,1))

name = "Biraj"
age = 18

print(f"Hi my name is  {name}. I am {age} years old ")