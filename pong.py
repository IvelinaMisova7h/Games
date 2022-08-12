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
paddle_a.penup()     # No drawing when moving
paddle_a.goto(-350, 0)

# Paddle B



# Ball





# Main game loop
while True:
    window.update()
