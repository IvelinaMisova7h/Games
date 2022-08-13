import turtle

window = turtle.Screen()
window.title("Pong by @Ivelina")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(False)      # Speed up

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)    # Speed of animation. Sets the speed to the max.
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()     # No drawing when moving
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = paddle_a.clone()
paddle_b.color('blue')
paddle_b.setx(350)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1   # User defined object properties
ball.dy = 1

# Function


def paddle_a_up():
    y = paddle_a.ycor()   # Returns the y coordinates. ycor() method is from the turtle.
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.onkeypress(paddle_a_up, 'w')
window.onkeypress(paddle_a_down, 's')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')
window.listen()

# Main game loop
while True:
    def move():
        x, y = ball.position()
        ball.setposition(x + ball.dx, y + ball.dy)
    window.update()
    window.ontimer(move)
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
