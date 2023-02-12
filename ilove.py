from turtle import *
import turtle

# draw I
def draw_I():
    turtle.penup()
    turtle.goto(-50, 100)

    turtle.fillcolor("blue")

    turtle.begin_fill()
    turtle.pendown()
    # Draw the I
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)

    turtle.end_fill()
    
# draw love symbol
def draw_love_symbol():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(30, -20)
    turtle.pendown()

    turtle.fillcolor("red")
    # Draw the heart shape
    turtle.begin_fill()  
    turtle.left(50)
    turtle.forward(80)
    turtle.circle(-40, 200)
    turtle.setheading(60)
    turtle.circle(-40, 200)
    turtle.forward(80)
    turtle.end_fill()

    # turtle.pendown()

# draw U
def draw_U():
    turtle.penup()
    turtle.goto(140, 100)
    turtle.pendown()
    turtle.fillcolor("blue")
    # Draw the U shape
    turtle.begin_fill()
    turtle.left(140)
    turtle.backward(20)
    turtle.right(90)
    turtle.forward(60)
    turtle.circle(60, 90)
    turtle.forward(1)
    turtle.circle(60, 90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(60)
    turtle.circle(-40, 90)
    turtle.forward(1)
    turtle.circle(-40, 90)
    turtle.forward(60)
    turtle.end_fill()
    
draw_I()
draw_love_symbol()
draw_U()

turtle.exitonclick()