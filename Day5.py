#Using the for loop with Python Lists
fruits = ["apple" , "mango" , "orange"]
for fruit in fruits:
    print (fruit)

    fruits1 = ["apple", "banana", "cherry"]
for index, fruit1 in enumerate(fruits1):
    print(f"{index}: {fruit1}")


#For Loops and the range() Function
for i in range(10):
    print (i)

for j in range(2, 11, 2):  # 2, 4, 6, 8, 10
    print(j)

#Combining Lists and range()
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")


numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"Total: {total}") 

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")




