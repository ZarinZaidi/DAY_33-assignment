# using turtle module easier for beginner. no need to install like pygame.
import turtle

# setup for the game windows
wn = turtle.Screen()
wn.title('PONG! by Zarin')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) 
# tracer stops the window from updating. so we hv to manually update it.speed up our game a bit.


# Paddle A
paddle_a = turtle.Turtle() #turtle object. Class name: Turtle
paddle_a.speed(0) #speed of animation. sets the speed to the maxi possible speed
paddle_a.shape('square') # by default shape is 25px x 25px
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len= 1) #stretch the paddle size
paddle_a.penup()
paddle_a.goto(-350, 0) #paddle a starts at coordinate (x, y)

# Paddle B
paddle_b = turtle.Turtle() #turtle object. Class name: Turtle
paddle_b.speed(0) #speed of animation. sets the speed to the maxi possible speed
paddle_b.shape('square') # by default shape is 25px x 25px
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len= 1) #stretch the paddle size
paddle_b.penup()
paddle_b.goto(+350, 0) #paddle a starts at coordinate (x, y)

# Ball
ball = turtle.Turtle() #turtle object. Class name: Turtle
ball.speed(0) #speed of animation. sets the speed to the maxi possible speed
ball.shape('square') # by default shape is 25px x 25px
ball.color('white')
ball.penup()
ball.goto(0, 0) #ball a starts at coordinate (x, y)

# Main game loop
while True:
    wn.update()