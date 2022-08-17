import turtle

delay = 0.1

# Score
score = 0
high_score = 0

# Creating the screen
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("green")
screen.setup(width=600, height=800)
screen.tracer(0)  # Turns screen updates

# Creating the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("purple")
snake.penup()      # No drawing when moving
snake.goto(0, 0)
snake.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High score: 0", align="center", font=("Courier", 24, "normal"))
