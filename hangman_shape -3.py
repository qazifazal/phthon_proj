import turtle
 
t = turtle.Turtle()
rope_position = t.pos()
def MAIN():
  PANSIGOT()
  DRAW_HEAD("#ffffff", 30, 0, 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
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


  

#THIS CODE FOR PANSIGOT.

def PANSIGOT():
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
  return

def ROPE():
  t.penup()
  t.backward(50)
  t.right(90)
  t.goto(0, 250)
  t.pendown()
  t.pensize(2)
  t.forward(50)

  t.penup()
  t.goto(-50, 150)
  t.pendown()
  t.circle(50)
  t.right(270)





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

#MAIN()


import subprocess as sp
print("Hey! Man Please Enter Your Choice: ")

mode = input("Enter mode:\n'e' for easy ,'h' for hard and 'm' for medium: ")
if mode == 'e':
    file = open('easy.txt')
    #Wordscount Will count the Number of Lines in Given file: 
    wordsCount = sum(1 for line in file)
    file.close()
    
    file = open('easy.txt', 'r')
    wordsList = ['none'] * wordsCount
    
    for word in range(wordsCount):
        
        name = file.readline()
        wordsList[word] = name
        name = wordsList[word].rstrip('\n')
        
        length = len(name)
        spaces = ""
        for wordLength in range(length):
            spaces += '-'
        print(spaces)
        
        tries = 6
        while(tries > 0):
            print("Tries Remaining:", tries)
            char = input("Enter an alphabet: ").lower()
            
            for i in range(length):
                if char == name[i]:
                    #spaces = spaces.replace(spaces[i], char, 1)
                    spaces = spaces[:i] + char + spaces[i + 1:]
                    print(spaces)
                    
                elif char not in name:
                    tries -= 1
                    if tries == 5:
                        PANSIGOT()
                    elif tries == 4:
                        DRAW_HEAD(30, 0, 100)
                    elif tries == 3:
                        RECTANGLE()
                    elif tries == 2:
                        LEFT_RIGHT_ARM()
                    elif tries == 1:
                        LEFT_RIGHT_LEG()
                    elif tries == 0:
                        ROPE()
                    break
            if spaces == name:
                print("Congrats, you chose the word!")
                break
                
                
        if spaces == name:
            again = input("Do you want to go for next guess?\nEnter 'y' for yes and 'n' for no: ")
            if again != 'y':
                break
        if spaces != name:
            print("Sorry, good luck for next time.")
            break
        
        print()
    file.close()

#THE BELOW CODE FOR MEDIUM LEVEL
if mode == 'm':
    file = open('medium.txt')
    wordsCount = sum(1 for line in file)
    file.close()
    
    file = open('medium.txt', 'r')
    wordsList = ['none'] * wordsCount
    
    for word in range(wordsCount):
        
        name = file.readline()
        wordsList[word] = name
        name = wordsList[word].rstrip('\n')
        
        length = len(name)
        spaces = ""
        for wordLength in range(length):
            spaces += '-'
        print(spaces)
        
        tries = 4
        while(tries > 0):
            print("Tries Remaining:", tries)
            char = input("Enter an alphabet: ").lower()
            
            for i in range(length):
                if char == name[i]:
                    #spaces = spaces.replace(spaces[i], char, 1)
                    spaces = spaces[:i] + char + spaces[i + 1:]
                    print(spaces)
                    
                elif char not in name:
                    tries -= 1
                    if tries == 3:
                        PANSIGOT()
                        DRAW_HEAD(30, 0, 100)
                        HAT()
                    elif tries == 2:
                        RECTANGLE()
                        LEFT_RIGHT_ARM()
                    elif tries == 1:
                        LEFT_RIGHT_LEG()
                    elif tries == 0:
                        ROPE()
                    break
            if spaces == name:
                print("Congrats, you chose the word!")
                break
                
                
        if spaces == name:
            again = input("Do you want to go for next guess?\nEnter 'y' for yes and 'n' for no: ")
            if again != 'y':
                break
        if spaces != name:
            print("Sorry, good luck for next time.")
            break
        
        print()
    file.close()




#The below code is for hard level
elif mode == 'h':
    num_lines = sum(1 for line in open('hard.txt'))
    file = open('hard.txt')
    wordsCount = sum(1 for line in file)
    file.close()
    
    file = open('easy.txt', 'r')
    wordsList = ['none'] * wordsCount
    
    for word in range(wordsCount):
        
        name = file.readline()
        wordsList[word] = name
        name = wordsList[word].rstrip('\n')
        
        length = len(name)
        spaces = ""
        for wordLength in range(length):
            spaces += '-'
        print(spaces)
        
        tries = 3
        while(tries > 0):
            print("Tries Remaining:", tries)
            char = input("Enter an alphabet: ").lower()
            
            for i in range(length):
                if char == name[i]:
                    spaces = spaces[:i] + char + spaces[i + 1:]
                    print(spaces)
                    
                elif char not in name:
                    tries -= 1
                    if tries == 2:
                      PANSIGOT()
                      DRAW_HEAD(30, 0, 100)#WHEN FUNCTION CALLED THE HEAD OF MAN WILL DRAW
                      HAT()
                      RECTANGLE()#RECTANGLE CODE SHOW BELLY + CHEST etc.
                       
                    elif tries == 1:
                        LEFT_RIGHT_ARM()
                        LEFT_RIGHT_LEG()
                        
                    elif tries == 0:
                        ROPE()
                    break
            if spaces == name:
                print("Congrats, you chose the word!")
                break
                
                
        if spaces == name:
            again = input("Do you want to go for next guess?\nEnter 'y' for yes and 'n' for no: ")
            if again != 'y':
                break
        if spaces != name:
            print("Sorry, good luck for next time.")
            break
        
        print()
    file.close()

#If user enters any other input except 'e' and 'h' in start time then this piece of code will be executed.
else:
    print("Sorry, invalid input!")
