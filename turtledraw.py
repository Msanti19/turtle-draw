
import turtle
import math

def distance_between_points(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

TEXTFILENAME = 'turtle-draw.txt'

print('Turtle Draw Starting...')




turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()

print ('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

      
        turtleDraw.color(color)
        turtleDraw.goto(x,y)
        turtleDraw.pendown()


    if (len(parts) == 1):
        turtleDraw.penup()



    line = line = turtleDrawTextfile.readline()

turtle.done()
turtleDrawTextfile.close()

#wait
print ('\nEnd')