def greet():
    return "Hello!"

def execute_function(func):
    print(func())

execute_function(greet)



import turtle

def move_forward():
    t.forward(10)

t = turtle.Turtle()
screen = turtle.Screen()
screen.listen()  # Activates the event listener
screen.onkey(move_forward, "Up")  # Moves forward when "Up" arrow key is pressed
screen.exitonclick()


class Dog:
    def __init__(self, name):
        self.name = name
        self.energy = 10  # Initial state

    def bark(self):
        if self.energy > 0:
            print(f"{self.name} says Woof!")
            self.energy -= 1
        else:
            print(f"{self.name} is too tired to bark!")

# Creating instances
dog1 = Dog("Buddy")
dog2 = Dog("Max")

dog1.bark()  # Changes dog1's energy state
dog2.bark()  # Changes dog2's energy state



import turtle
t = turtle.Turtle()
t.goto(100, 100)  # Moves the turtle to (100, 100)


t.penup()
t.goto(-50, -50)
t.pendown()

for _ in range(4):
    t.forward(100)
    t.left(90)




## Project 


import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.setup(width=500, height=400)

# Create two turtles
player1 = turtle.Turtle(shape="turtle")
player2 = turtle.Turtle(shape="turtle")

# Set initial positions
player1.penup()
player1.goto(-200, 100)
player2.penup()
player2.goto(-200, -100)

# Functions to move turtles
def move_player1():
    player1.forward(random.randint(10, 20))

def move_player2():
    player2.forward(random.randint(10, 20))

# Key bindings
screen.listen()
screen.onkey(move_player1, "Up")
screen.onkey(move_player2, "Down")

# Finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.hideturtle()
finish_line.goto(200, 150)
finish_line.setheading(270)
finish_line.pendown()
finish_line.forward(300)

screen.exitonclick()

