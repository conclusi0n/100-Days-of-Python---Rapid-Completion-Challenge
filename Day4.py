import random 

#random.randint(a, b)
number = random.randint(1,10)
print (number)

# random.random()
random_float = random.random()
print (random_float)

#random.choice(sequence)

colors = ["red","blue","green"]
random_colors = random.choice(colors)
print (random_colors)

#random.shuffle(sequence)

numbers = [1,2,3,4,5,6,7]
apple = random.shuffle(numbers)
print (numbers)

#Understanding Offset and Appending Items to Lists
#Offset in Lists (Indexing)
fruits = ["Apple" , "Mango","Pineapple"]
print (fruits)
print (fruits[0])
print (fruits[1])
print (fruits[2])


#Appending Items to Lists

append_number = [1,2,3,4]
print (append_number)
append_number.append (5)
print (append_number)
append_number.extend([6,7,8])
print(append_number)


#Index Errors and Working with Nested Lists

fruits = ["apple", "banana", "cherry"]
# (It has an error )print(fruits[3]) 
print(fruits)
index = 2
if index < len(fruits):
    print(fruits[index])  # Output: cherry
else:
    print("Index out of range.")


    #Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[2])       # Output: [1, 2, 3] (first row)
print(matrix[1][2])    # Output: 6 (second row, third column)

for row in matrix:
    for item in row:
        print(item, end="")  # Output: 1 2 3 4 5 6 7 8 9

