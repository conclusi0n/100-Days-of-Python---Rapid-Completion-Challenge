#Understanding Turtle Graphics

import turtle as t
t.colormode(255)  # Enable RGB color mode (values from 0-255)


t.forward(100)  # Move forward by 100 units
t.back(50)  # Move backward by 50 units
t.right(90)     # Turn right by 90 degrees
t.left(45) 
t.goto(20, 30)     # Turn left by 45 degrees
t.dot(20)       # Draw a dot with a diameter of 20
t.circle(50)    # Draw a circle with a radius of 50


t.penup()       # Lift the pen to stop drawing
t.pendown()     # Put the pen down to start drawing
    # Move to specific coordinates (x, y)
t.setheading(90)  # Set the direction (0° = east, 90° = north, etc.)

#2. Importing Modules, Installing Packages, and Using Aliases
import turtle  # Import the Turtle Graphics module
from random import choice
import colorgram
##colors = colorgram.extract('image.jpg', 10)  # Extract 10 colors from an image

#3. Python Tuples and Immutable Data
# Example: RGB color as a tuple
rgb_color = (255, 100, 0)  # Red
print(rgb_color[1])  # Access the red component (255)

import random
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(random_color)  # Example output: (123, 200, 50)




#new start 

import turtle as t
import random

# Setting up the Turtle
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# List of colors
color_list = [(236, 248, 243), (36, 95, 183), (236, 165, 79), (244, 223, 87), 
              (215, 69, 105), (98, 197, 234), (250, 51, 22), (203, 70, 21), 
              (240, 106, 143), (185, 47, 90), (143, 233, 216), (252, 136, 166), 
              (165, 175, 233), (66, 45, 13), (72, 205, 170), (83, 187, 100), 
              (20, 156, 51), (24, 36, 86), (252, 220, 0), (164, 28, 8), 
              (105, 39, 44), (250, 152, 2), (22, 151, 229), (108, 213, 249), 
              (254, 12, 3), (38, 48, 98), (98, 96, 186)]

# Function to draw a single dot
def draw_dot(color):
    tim.dot(20, color)

# Function to move the turtle to the next row
def move_to_next_row(start_x, start_y, row_number, spacing):
    new_y = start_y + (row_number * spacing)
    tim.goto(start_x, new_y)

# Main function to draw the dot painting
def draw_painting(rows, cols, dot_size, spacing):
    start_x = -cols * spacing // 2  # Center horizontally
    start_y = -rows * spacing // 2  # Center vertically

    for row in range(rows):
        move_to_next_row(start_x, start_y, row, spacing)
        for col in range(cols):
            draw_dot(random.choice(color_list))
            tim.forward(spacing)

# Draw a 10x5 grid of dots
draw_painting(rows=5, cols=10, dot_size=20, spacing=50)

# Set up the screen to wait for a click before closing
screen = t.Screen()
screen.exitonclick()


