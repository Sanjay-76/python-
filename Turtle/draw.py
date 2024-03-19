import turtle as t
# Set up the turtle
t.speed(1)
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart
t.begin_fill()
t.fillcolor("red")
t.pensize(2)
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Draw the arrow stem
t.pendown()
t.goto(0, 250)
t.penup()
t.pensize(3)
t.right(-70)
t.forward(100)

# Draw the arrowhead
t.begin_fill()
t.fillcolor("red")
t.right(180)
t.forward(40)
t.right(120)
t.forward(40)
t.end_fill()

# Hide the turtle and display the drawing
t.hideturtle()
t.done()


# Set up the turtle
t.speed(10)
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart
t.begin_fill()
t.fillcolor("red")
t.pensize(2)
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Hide the turtle and display the drawing
t.hideturtle()
t.done()
import turtle as t

# Set up the turtle
t.speed(1)
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the heart
t.begin_fill()
t.fillcolor("red")
t.pensize(2)
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Hide the turtle and display the drawing
t.hideturtle()
t.done()
