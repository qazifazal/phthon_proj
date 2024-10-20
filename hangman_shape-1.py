import turtle
 
t = turtle.Turtle()

def draw_circle(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()


#p_got
t.penup()
t.goto(-250, -150)
t.pendown()

t.fillcolor('black')
t.begin_fill()
t.pensize(5)
t.forward(300)
t.right(90)
t.forward(70)
t.right(90)
t.forward(300)
t.right(90)
t.forward(70)
t.end_fill()

t.right(90)
t.forward(120)

t.left(90)
t.forward(400)
t.right(90)
t.forward(180)
t.penup()

t.backward(50)
t.right(90)
t.pendown()
t.pensize(2)
t.forward(50)

t.penup()
t.goto(-50, 150)
t.pendown()
t.circle(50)
t.right(270)

#Below statement for drawing snowman body
draw_circle("#ffffff", 30, 0, 100)

#Rectangle
t.penup()
t.goto(-25, 100)
t.pendown()
t.forward(50) #Forward turtle by 50 units
t.right(90) #Turn turtle by 90 degree
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(100)
t.right(90)
 
draw_circle("black", 2, -10, 130) #Drawing left eye
draw_circle("black", 2, 10, 130) #Drawing right eye
#triangle
t.penup()
t.goto(-3, 125)
t.pendown()
t.forward(6) # draw base
t.left(110)
t.forward(10)
t.left(150)
t.forward(10)
t.left(100)
#Mouth
t.penup()
t.goto(-8, 120)
t.right(90)
t.pendown()
t.circle(8, 180)
t.right(90)
 
#Below three statements for drawing buttons
draw_circle("red", 2, 0, 85)
draw_circle("red", 2, 0, 75)
draw_circle("red", 2, 0, 65)
 
#Code for drawing left arm
t.penup()
t.goto(-15, 85)
t.pendown()
t.pensize(5)
t.goto(-75, 50)
#Code for drawing right arm
t.penup()
t.goto(15, 85)
t.pendown()
t.pensize(5)
t.goto(75, 50)

#Code for drawing left leg
t.penup()
t.goto(-15, 0)
t.pendown()
t.pensize(5)
t.goto(-45, -70)
#Code for drawing right leg
t.penup()
t.goto(15, 0)
t.pendown()
t.pensize(5)
t.goto(45, -70)
 
#Code for drawing hat
t.penup()
t.goto(-35, 148)
t.color("green")
t.pensize(6)
t.pendown()
t.goto(35, 148)
 
t.goto(30, 148)
t.fillcolor("green")
t.begin_fill()
t.left(90)
t.forward(15)
t.left(90)
t.forward(60)
t.left(90)
t.forward(15)
t.end_fill()
