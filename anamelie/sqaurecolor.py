import turtle
t = turtle.Pen( )
turtle.bgcolor("white")
t.speed(0)
colors = [ "red" , "purple" , "blue" , "green"]
for x in range (100) :
    t.pencolor ( colors[ x % 4]  )
    t.circle (2*x)
    t.left(91)
