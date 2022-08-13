from turtle import Screen, Turtle

# Functions
def paddle_a_up():
    paddle_a.forward(20)

def paddle_a_down():
    paddle_a.backward(20)

def paddle_b_up():
    paddle_b.forward(20)

def paddle_b_down():
    paddle_b.backward(20)

# Main loop
def move():
    x, y = ball.position()
    ball.setposition(x + ball.dx, y + ball.dy)

    screen.update()
    screen.ontimer(move)

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(False)

# Paddle A
paddle_a = Turtle()
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=1, stretch_len=5)
paddle_a.setheading(90)
paddle_a.penup()
paddle_a.color('red')
paddle_a.setx(-350)

# Paddle B
paddle_b = paddle_a.clone()
paddle_b.color('blue')
paddle_b.setx(350)

# Ball
ball = Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()

ball.dx = 1  # user defined object properties
ball.dy = 1

# Keyboard binding
screen.onkeypress(paddle_a_up, 'w')
screen.onkeypress(paddle_a_down, 's')
screen.onkeypress(paddle_b_up, 'Up')
screen.onkeypress(paddle_b_down, 'Down')
screen.listen()

move()

screen.mainloop()