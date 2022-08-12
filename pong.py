import turtle

window = turtle.Screen()
window.title("Pong by @Ivelina")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)      # Speed up

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)    # Speed of animation. Sets the speed to the max.
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()     # No drawing when moving
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)




# Main game loop
while True:
    window.update()
