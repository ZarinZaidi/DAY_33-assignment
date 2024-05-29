import turtle #using turtle module easier for beginner. no need to install like pygame.
import winsound #to use sound
# import os #to use sound on Linux/Mac

# setup for the game windows
wn = turtle.Screen()
wn.title('PONG! by Zarin')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) 
# tracer stops the window from updating. so we hv to manually update it.speed up our game a bit.

# Score
score_a = 0
score_b = 0

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
paddle_b.goto(+350, 0) #paddle b starts at coordinate (x, y)

# Ball
ball = turtle.Turtle() #turtle object. Class name: Turtle
ball.speed(0) #speed of animation. sets the speed to the maxi possible speed
ball.shape('square') # by default shape is 25px x 25px
ball.color('white')
ball.penup()
ball.goto(0, 0) #ball a starts at coordinate (x, y)
# separate the ball movements into parts (x move & y move)
ball.dx = 0.1 #ball move by 0.1px on x-axis
ball.dy = 0.1 #ball move by 0.1px on y-axis

# Pen
pen = turtle.Turtle() #turtle object. Class name: Turtle
pen.speed(0) #speed of animation. sets the speed to the maxi possible speed
pen.color('white')
pen.penup() #don/t draw the lines when the pen moves
pen.hideturtle() #hide the object. we just want to see the text
pen.goto(0, 275) #within windows  size
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 15, 'normal')) #Default score on the screen


# Function
def paddle_a_up():
    y = paddle_a.ycor() #know the current y coordinate
    y += 25 #adds 20px to y coor
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor() #know the current y coordinate
    y -= 25 #adds 20px to y coor
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor() #know the current y coordinate
    y += 25 #adds 20px to y coor
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor() #know the current y coordinate
    y -= 25 #adds 20px to y coor
    paddle_b.sety(y)
    
# Update the score display
def update_score():
    pen.clear()  # Clear the pen first so the score won't overlap
    pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 15, 'normal'))  # Display updated score
    
# Keyboard binding
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, 'a') #call the fx when user press 'a'
wn.onkeypress(paddle_a_down, 'z') #call the fx when user press 'z'
wn.onkeypress(paddle_b_up, 'Up') #call the fx when user press 'Up' arrow key
wn.onkeypress(paddle_b_down, 'Down') #call the fx when user press 'Down' arrow key


# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border checking
    # top border
    if ball.ycor() > 290: #windows is y=300 and ball is 20/2=10
        ball.sety(290) #set it back to 290
        ball.dy *= -1 #to reverse the ball's direction
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC) #play sound
        # os.system('afplay bounce.wav) #play sound for Mac
        # os.system('aplay bounce.wav) #play sound for Linux
        
        
    # bottom border
    if ball.ycor() < -290: #windows is y=600/2=300 and ball is 20/2=10
        ball.sety(-290) #set it back to 290
        ball.dy *= -1 #to reverse the ball's direction
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC) #play sound
        # os.system('afplay bounce.wav) #play sound for Mac
        # os.system('aplay bounce.wav) #play sound for Linux
        
        
    # right border
    if ball.xcor() > 390: #windows is x=800/2=400 and ball is 20/2=10
        ball.goto(0, 0) #put the ball back to center
        ball.dx *= -1 #reverse the ball's direction
        score_a +=1 #player A(left) got 1 score if the ball goes off the right side
        update_score()
        
        
    # left border
    if ball.xcor() < -390: #windows is x=800/2=400 and ball is 20/2=10
        ball.goto(0, 0) #put the ball back to center
        ball.dx *= -1 #reverse the ball's direction
        score_b +=1 #player B(right) got 1 score if the ball goes off the left side
        update_score
        
           
    # Paddle and ball collisions detection
    # right paddle detection
    # if the ball's and paddles' edges are touching AND is the ball between the top and bottom of the paddle(size=100/2=50 but minus ball size=20/2=10)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): 
        ball.setx(340) #set it back to 340
        ball.dx *= -1 #reverse and bounce back the ball
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC) #play sound
        # os.system('afplay bounce.wav) #play sound for Mac
        # os.system('aplay bounce.wav) #play sound for Linux
        
        
    # left paddle detection
    # if the ball's and paddles' edges are touching AND is the ball between the top and bottom of the paddle(size=100/2=50 but minus ball size=20/2=10)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): 
        ball.setx(-340) #set it back to -340
        ball.dx *= -1 #reverse and bounce back the ball
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC) #play sound
        # os.system('afplay bounce.wav) #play sound for Mac
        # os.system('aplay bounce.wav) #play sound for Linux