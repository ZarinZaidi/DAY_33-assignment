# using turtle module easier for beginner. no need to install like pygame.
import turtle

# setup for the game windows
wn = turtle.Screen()
wn.title('PONG! by Zarin')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0) 
# tracer stops the window from updating. so we hv to manually update it.speed up our game a bit.

