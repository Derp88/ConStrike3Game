#Conflicting Strike(V5)
#Created by Dylan Barkley, Ethan Parvin, Caleb Obenchain
#Creation Date: 12/13/2020 @ 9:19 PM

#Major Changes
# +Add a death system
# +And collison system

#Imports
import turtle as trtl
import gun
import AI
#Variables
gameOver = False


#WN Background Setup
wn = trtl.Screen()
wn.bgcolor("Black")
background = "iceMap.gif"
wn.bgpic(background)
wn.tracer(0)

#Turtle Init

    #Player Turtle
player = trtl.Turtle()
player.color("White")
player.penup()
player.goto(0,-310)
player.setheading(90)

#playerGun.shapesize(10,20,1)
    #Hostile Turtles
hostile1 = trtl.Turtle()
hostile1.color("Purple")
hostile1.penup()
hostile1.goto(0,300)

hostile2 = trtl.Turtle()
hostile2.color("Purple")
hostile2.penup()
hostile2.goto(300,0)

hostile3 = trtl.Turtle()
hostile3.color("Purple")
hostile3.penup()
hostile3.goto(-300,0)


#Health Variables
playerStatus = "Alive"
hostile1Status = "Alive"
hostile2Status = "Alive"
hostile3Status = "Alive"

#Input Functions
def mouseAim(X,Y):
   
    player.setheading(player.towards(X,Y))
    
    gun.generateBullet(player.xcor(),player.ycor(),player.heading())
def playerUp():
    currentX = player.xcor()
    currentY = player.ycor()
    if currentY < 300:
        player.setposition(currentX, currentY+1)
    #coordinates()
    wn.update()
def playerDown():
    currentX = player.xcor()
    currentY = player.ycor()
    if currentY > -291:
        player.setposition(currentX, currentY-1)
    #coordinates()
    wn.update()
def playerLeft():
    currentX = player.xcor()
    currentY = player.ycor()
    player.setposition(currentX-1, currentY)
    #coordinates()
    wn.update()
def playerRight():
    currentX = player.xcor()
    currentY = player.ycor()
    player.setposition(currentX+1, currentY)
    #coordinates()
    wn.update()
def coordinates ():
    print ("X = " + str(player.xcor()))
    print ("Y = " + str(player.ycor()))
    wn.update()

def AIrun():
    
    if hostile1Status == "Alive":
        AI.aiMove(hostile1, player.xcor(),player.ycor())
    else:
        hostile1.hideturtle()

    if hostile2Status == "Alive":
        AI.aiMove(hostile2, player.xcor(),player.ycor())
    else:
        hostile2.hideturtle()

    if hostile3Status == "Alive":
        AI.aiMove(hostile3, player.xcor(),player.ycor())
    else:
        hostile3.hideturtle()

    if playerStatus != "Alive":
        player.hideturtle()

def aliveCheck():
    global hostile1Status
    global hostile2Status
    global hostile3Status
    global playerStatus
    global gameOver
    #NOTICE!
    #THIS IS SLIGHTLY BROKEN AND MAINLY WORKS
    #COULD USE SOME IMPROVMENT

    if hostile1.distance(gun.BulletX, gun.BulletY) < 10 and abs(hostile1.heading() - gun.BulletHeading) > 10:
        hostile1Status = "Dead"
    if hostile2.distance(gun.BulletX, gun.BulletY) < 10 and abs(hostile2.heading() - gun.BulletHeading) > 10:
        hostile2Status = "Dead"
    if hostile3.distance(gun.BulletX, gun.BulletY) < 10 and abs(hostile3.heading() - gun.BulletHeading) > 10:
        hostile3Status = "Dead"
    if player.distance(gun.BulletX, gun.BulletY) < 10 and abs(player.heading() - gun.BulletHeading) > 10: 
        playerStatus = "Dead"
        gameOver = True



#Main repeating loop
def mainPerodic():
    
    while gameOver != True:
        #Moves all bullets
        gun.moveBullet()
      
        #Checks if turtle alive
        aliveCheck()

        #Controls AI
        AIrun()

#Inputs
wn.onkeypress(playerUp, "w")
wn.onkeypress(playerDown, "s")
wn.onkeypress(playerLeft, "a")
wn.onkeypress(playerRight, "d")
wn.onscreenclick(mouseAim)
wn.listen()

#Main loop
if gameOver != True:
    mainPerodic()
