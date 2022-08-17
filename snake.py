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

