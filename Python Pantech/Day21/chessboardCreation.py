#A chessboard is the type of game board used for the game of chess,on which pawns and chess pieces are placed.
#Chessboard is divided into 64 squares and has a squared shape.Subdivisions in this place are painted in contrasted hues.We shall create a turtle-shaped chessboard with this in mind.
#A chessboard is usually square,with an alternating pattern of squares of two colours.
#For creating a chessboard,I will use two Python libraries;Metplotlib for visualization,NumPy for building an algorithm which will help us to craete and visulaize a chessboard.
#Python comes with module called Turtle.It offers drawing with a cardboard screen and a turtle(pen).Move the turtle to create anything on the screen(pen).There are other functions,such as forward() and backward(),to move the turtle.

#import turtle
import turtle
#Set a screen to draw the chess board on it and craete a turtle instance for our program.
scr=turtle.Screen()
ttl=turtle.Turtle()


#draw() method for drawing squares.
def draw():
    for i in range(4):
        ttl.forward(35)
        ttl.left(90)

    ttl.forward(35)

#Main driving code
if __name__=="__main__":
    scr.setup(500,700)
    ttl.speed(90)
    for j in range(8):
        ttl.up()
        ttl.setpos(-110,35 * j)
        ttl.down()
        for k in range(8):
            if(j+k)%2==0:
                clr='black'
            else:
                clr='white'
            ttl.fillcolor(clr)
            ttl.begin_fill()
            draw()
            ttl.end_fill()
    ttl.hideturtle()
    turtle.done()




