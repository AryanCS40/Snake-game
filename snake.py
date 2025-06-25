import turtle
import random
import time

delay=0.1
sc=0
hs=0
bodies=[]

#creating a screen
s = turtle.Screen()
s.title("The snake game.")
s.bgcolor("white")
s.setup(width=600,height=600)  #size of a screen

#creating head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

#creating food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.ht() #hide turtle
food.goto(150,200)
food.st() #show turtle

#creating a score board
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250,250)
sb.write("Score : 0 | Highest Score : 0") #print the score on screen for the 1st time.

#Game over message
message = turtle.Turtle()
message.penup()
message.ht()
message.goto(0,50)

#creating functions for moving 
def moveUp():
    if head.direction != "down":
        head.direction = "up"
def moveDown():
    if head.direction != "up":
        head.direction = "down"
def moveRight():
    if head.direction != "left":
        head.direction = "right"
def moveLeft():
    if head.direction != "right":
        head.direction = "left"
def moveStop():
    head.direction = "stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction =="left":
        x =head.xcor()
        head.setx(x-20)
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction =="right":
        x = head.xcor()
        head.setx(x+20)

#event handling
s.listen()
s.onkey(moveUp,"Up")
s.onkey(moveDown,"Down")
s.onkey(moveLeft,"Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

#main loop
while True:
   
    s.update() #to update the screen
   
    #check collision with the borders
    if head.xcor()>290:
        head.setx(-290)
    
    if head.xcor()<-290:
        head.setx(290)
    
    if head.ycor()>290:
        head.sety(-290)
    
    if head.ycor()<-290:
        head.sety(290)
    
    #check collision with the  food
    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        
        #increase the body of snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("green")
        bodies.append(body) #append the new body in the list

        sc=sc+100 #update the score
        delay=delay-0.0001 #boost the speed of snake 

        if sc>hs:
            hs = sc #update the highest score
        sb.clear()
        sb.write("Score : {} | Highest Score : {}".format(sc,hs))
    
    #move snake bodies
    for i in range(len(bodies)-1 ,0,-1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    #check collision with the snake body
    for body in bodies:
        if body.distance(head)<20:
            message.write("Game over....")
            message.clear()
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #Hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("Score : {}  |  Highest Score : {}".format(sc,hs))
    time.sleep(delay)
            
s.mainloop()

            
                
            

    

