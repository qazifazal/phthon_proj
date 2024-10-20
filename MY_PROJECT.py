import turtle
 
t = turtle.Turtle()

def MAIN1():
 
  DRAW_HEAD( 30, -200, 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
  RECTANGLE()#RECTANGLE CODE SHOW BELLY + CHEST etc.
  LEFT_RIGHT_ARM()
  LEFT_RIGHT_LEG()
  HAT()


#Button
def DRAW_BUTTON(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

#THIS CODE FOR HEAD OF MAN

def DRAW_HEAD(radius, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.circle(radius)
  
#LEFT EYE
  t.penup()
  t.goto(-210,130)
  t.pendown()
  t.circle(2)
  
#RIGGHT EYE
  t.penup()
  t.goto(-190,130)
  t.pendown()
  t.circle(2)
  
#THIS CODE FOR MOUTH OF MAN.

  #t.penup()
  #t.goto(-208, 120)
  #t.right(90)
  #t.pendown()
  #t.circle(192, 180)
  #t.right(90)
#THIS CODE FOR NOSE OF MAN.

  t.penup()
  t.goto(-203, 125)
  t.pendown()
  t.forward(6) #DRAW BASE OF NOSE.
  t.left(110)
  t.forward(10)
  t.left(150)
  t.forward(10)
  t.left(100)

#HAT
  HAT()


  







#RECTANGLE CODE SHOW BELLY + CHEST etc. 

def RECTANGLE():
  t.penup()
  t.goto(-225, 100)
  t.pendown()
  t.forward(50) 
  t.right(90)   
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(90)
#BELOW THREE STATEMENT ARE FOR BUTTON. 
  DRAW_BUTTON("red", 2, -200, 85)
  DRAW_BUTTON("red", 2, -200, 75)
  DRAW_BUTTON("red", 2, -200, 65)



 

 
#CODE FOR LEFT AND RIGHT ARM OF MAN

def LEFT_RIGHT_ARM():

#CODE FOR LEFT ARM.

  t.penup()
  t.goto(-215, 85)
  t.pendown()
  t.pensize(5)
  t.goto(-275, 50)

#CODE FOR RIGHT ARM.

  t.penup()
  t.goto(-185, 85)
  t.pendown()
  t.pensize(5)
  t.goto(-125, 50)


#THIS CODE FOR LEFT AND RIGHT LEG OF MAN.

def LEFT_RIGHT_LEG():

#CODE FOR LEFT LEG.

  t.penup()
  t.goto(-215, 0)
  t.pendown()
  t.pensize(5)
  t.goto(-245, -70)

#CODE FOR RIGHT LEG.

  t.penup()
  t.goto(-185, 0)
  t.pendown()
  t.pensize(5)
  t.goto(-155, -70)



#THIS CODE IS FOR HAT OF MAN.

def HAT():
  t.penup()
  t.goto(-235, 148)
  t.color("green")
  t.pensize(6)
  t.pendown()
  t.goto(-165, 148)
 
  t.goto(-170, 148)
  t.fillcolor("green")
  t.begin_fill()
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(60)
  t.left(90)
  t.forward(15)
  t.end_fill()
  t.left(90)

#MAIN1()

#############################################################Character 2)###########################


#import turtle
 
#t = turtle.Turtle()

def MAIN2():
 
  DRAW_HEAD( 30,200 , 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
  RECTANGLE()#RECTANGLE CODE SHOW BELLY + CHEST etc.
  LEFT_RIGHT_ARM()
  LEFT_RIGHT_LEG()
  HAT()


#Button
def DRAW_BUTTON(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

#THIS CODE FOR HEAD OF MAN

def DRAW_HEAD(radius, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.circle(radius)
  
#LEFT EYE
  t.penup()
  t.goto(190,130)
  t.pendown()
  t.circle(2)
  
#RIGGHT EYE
  t.penup()
  t.goto(210,130)
  t.pendown()
  t.circle(2)
  
#THIS CODE FOR MOUTH OF MAN.

#  t.penup()
 # t.goto(192, 120)
  #t.right(90)
  #t.pendown()
  #t.circle(208, 180)
  #t.right(90)
#THIS CODE FOR NOSE OF MAN.

  t.penup()
  t.goto(197, 125)
  t.pendown()
  t.forward(6) #DRAW BASE OF NOSE.
  t.left(110)
  t.forward(10)
  t.left(150)
  t.forward(10)
  t.left(100)

#HAT
  HAT()


  







#RECTANGLE CODE SHOW BELLY + CHEST etc. 

def RECTANGLE():
  t.penup()
  t.goto(175, 100)
  t.pendown()
  t.forward(50) 
  t.right(90)   
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(90)
#BELOW THREE STATEMENT ARE FOR BUTTON. 
  DRAW_BUTTON("red", 2, 200, 85)
  DRAW_BUTTON("red", 2, 200, 75)
  DRAW_BUTTON("red", 2, 200, 65)



 

 
#CODE FOR LEFT AND RIGHT ARM OF MAN

def LEFT_RIGHT_ARM():

#CODE FOR LEFT ARM.

  t.penup()
  t.goto(185, 85)
  t.pendown()
  t.pensize(5)
  t.goto(125, 50)

#CODE FOR RIGHT ARM.

  t.penup()
  t.goto(215, 85)
  t.pendown()
  t.pensize(5)
  t.goto(275, 50)


#THIS CODE FOR LEFT AND RIGHT LEG OF MAN.

def LEFT_RIGHT_LEG():

#CODE FOR LEFT LEG.

  t.penup()
  t.goto(185, 0)
  t.pendown()
  t.pensize(5)
  t.goto(155, -70)

#CODE FOR RIGHT LEG.

  t.penup()
  t.goto(215, 0)
  t.pendown()
  t.pensize(5)
  t.goto(245, -70)



#THIS CODE IS FOR HAT OF MAN.

def HAT():
  t.penup()
  t.goto(165, 148)
  t.color("yellow")
  t.pensize(6)
  t.pendown()
  t.goto(235, 148)
 
  t.goto(230, 148)
  t.fillcolor("red")
  t.begin_fill()
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(60)
  t.left(90)
  t.forward(15)
  t.end_fill()
  t.left(90)

#MAIN2()

def score():
  MAIN1()
  MAIN2()


####################################  CHARACTER 3############################


def MAIN3():
 
  DRAW_HEAD( 30, 0, 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
  RECTANGLE()#RECTANGLE CODE SHOW BELLY + CHEST etc.
  LEFT_RIGHT_ARM()
  LEFT_RIGHT_LEG()
  HAT()


#Button
def DRAW_BUTTON(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

#THIS CODE FOR HEAD OF MAN

def DRAW_HEAD(radius, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.circle(radius)
  
#LEFT EYE
  t.penup()
  t.goto(-10,130)
  t.pendown()
  t.circle(2)
  
#RIGGHT EYE
  t.penup()
  t.goto(10,130)
  t.pendown()
  t.circle(2)
  
#THIS CODE FOR MOUTH OF MAN.

  t.penup()
  t.goto(-8, 120)
  t.right(90)
  t.pendown()
  t.circle(8, 180)
  t.right(90)
#THIS CODE FOR NOSE OF MAN.

  t.penup()
  t.goto(-3, 125)
  t.pendown()
  t.forward(6) #DRAW BASE OF NOSE.
  t.left(110)
  t.forward(10)
  t.left(150)
  t.forward(10)
  t.left(100)

#HAT
  HAT()


  







#RECTANGLE CODE SHOW BELLY + CHEST etc. 

def RECTANGLE():
  t.penup()
  t.goto(-25, 100)
  t.pendown()
  t.forward(50) 
  t.right(90)   
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(90)
#BELOW THREE STATEMENT ARE FOR BUTTON. 
  DRAW_BUTTON("red", 2, 0, 85)
  DRAW_BUTTON("red", 2, 0, 75)
  DRAW_BUTTON("red", 2, 0, 65)



 

 
#CODE FOR LEFT AND RIGHT ARM OF MAN

def LEFT_RIGHT_ARM():

#CODE FOR LEFT ARM.

  t.penup()
  t.goto(-15, 85)
  t.pendown()
  t.pensize(5)
  t.goto(-75, 50)

#CODE FOR RIGHT ARM.

  t.penup()
  t.goto(15, 85)
  t.pendown()
  t.pensize(5)
  t.goto(75, 50)


#THIS CODE FOR LEFT AND RIGHT LEG OF MAN.

def LEFT_RIGHT_LEG():

#CODE FOR LEFT LEG.

  t.penup()
  t.goto(-15, 0)
  t.pendown()
  t.pensize(5)
  t.goto(-45, -70)

#CODE FOR RIGHT LEG.

  t.penup()
  t.goto(15, 0)
  t.pendown()
  t.pensize(5)
  t.goto(45, -70)



#THIS CODE IS FOR HAT OF MAN.

def HAT():
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
  t.left(90)

#MAIN3()


####################################### CHARACTER 4#############################



def MAIN4():
 
  DRAW_HEAD( 30, 30, 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
  RECTANGLE()#RECTANGLE CODE SHOW BELLY + CHEST etc.
  LEFT_RIGHT_ARM()
  LEFT_RIGHT_LEG()
  HAT()


#Button
def DRAW_BUTTON(color, radius, x, y):
  t.penup()
  t.fillcolor(color)
  t.goto(x,y)
  t.pendown()
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

#THIS CODE FOR HEAD OF MAN

def DRAW_HEAD(radius, x, y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  t.circle(radius)
  
#LEFT EYE
  t.penup()
  t.goto(20,130)
  t.pendown()
  t.circle(2)
  
#RIGGHT EYE
  t.penup()
  t.goto(40,130)
  t.pendown()
  t.circle(2)
  
#THIS CODE FOR MOUTH OF MAN.

#  t.penup()
 # t.goto(22, 120)
 # t.right(90)
 # t.pendown()
 # t.circle(38, 180)
  #t.right(90)
#THIS CODE FOR NOSE OF MAN.

  t.penup()
  t.goto(27, 125)
  t.pendown()
  t.forward(6) #DRAW BASE OF NOSE.
  t.left(110)
  t.forward(10)
  t.left(150)
  t.forward(10)
  t.left(100)

#HAT
  HAT()


  







#RECTANGLE CODE SHOW BELLY + CHEST etc. 

def RECTANGLE():
  t.penup()
  t.goto(5, 100)
  t.pendown()
  t.forward(50) 
  t.right(90)   
  t.forward(100)
  t.right(90)
  t.forward(50)
  t.right(90)
  t.forward(100)
  t.right(90)
#BELOW THREE STATEMENT ARE FOR BUTTON. 
  DRAW_BUTTON("red", 2, 30, 85)
  DRAW_BUTTON("red", 2, 30, 75)
  DRAW_BUTTON("red", 2, 30, 65)



 

 
#CODE FOR LEFT AND RIGHT ARM OF MAN

def LEFT_RIGHT_ARM():

#CODE FOR LEFT ARM.

  t.penup()
  t.goto(15, 85)
  t.pendown()
  t.pensize(5)
  t.goto(-45, 50)

#CODE FOR RIGHT ARM.

  t.penup()
  t.goto(45, 85)
  t.pendown()
  t.pensize(5)
  t.goto(105, 50)


#THIS CODE FOR LEFT AND RIGHT LEG OF MAN.

def LEFT_RIGHT_LEG():

#CODE FOR LEFT LEG.

  t.penup()
  t.goto(15, 0)
  t.pendown()
  t.pensize(5)
  t.goto(-15, -70)

#CODE FOR RIGHT LEG.

  t.penup()
  t.goto(45, 0)
  t.pendown()
  t.pensize(5)
  t.goto(75, -70)



#THIS CODE IS FOR HAT OF MAN.

def HAT():
  t.penup()
  t.goto(-5, 148)
  t.color("brown")
  t.pensize(6)
  t.pendown()
  t.goto(65, 148)
 
  t.goto(60, 148)
  t.fillcolor("black")
  t.begin_fill()
  t.left(90)
  t.forward(15)
  t.left(90)
  t.forward(60)
  t.left(90)
  t.forward(15)
  t.end_fill()
  t.left(90)

#MAIN4()

def goodscore():
  MAIN3()
  MAIN4()


###################################GAME################################



import turtle
import time
import random

score = 0

delay = 0.1
if (score > 150):
  goodscore()
  
else:
  score()
# Score

high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Qazi Fazal.e.Qadir")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()





















