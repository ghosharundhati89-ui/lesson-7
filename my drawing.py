import turtle 
#creating canvas 
turtle.Screen().bgcolor("Blue")
sc=turtle.Screen()
sc. setup(500,200)
turtle.title ("welcome to turtle window")
board=turtle.Turtle()
#creating a square 
for i in range(4):
    board.forward(50)
    board.left(90)