import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle class
class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:  # Boundary limit
            self.sety(self.ycor() + 20)

    def go_down(self):
        if self.ycor() > -250:  # Boundary limit
            self.sety(self.ycor() - 20)

# Ball class
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.dx = 0.2
        self.dy = 0.2

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

# Score class
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=("Courier", 36, "normal"))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=("Courier", 36, "normal"))

    def left_point(self):
        self.left_score += 1
        self.update_score()

    def right_point(self):
        self.right_score += 1
        self.update_score()

# Create paddles, ball, and scoreboard
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Ball collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Ball collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # Ball goes out of bounds
    if ball.xcor() > 390:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.right_point()
        ball.reset_position()

# Exit on click
screen.exitonclick()
