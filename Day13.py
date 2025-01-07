#1st debugging 
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#2nd debugging 
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

#3dDebug

for number in range(1, 101):
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        print(number)

