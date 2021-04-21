import turtle as trtl

#To do list
#Weapons types: Shotgun, Assault Rifle, Pistol, Heavy Weapon, SMG
#Ammo in each weapon (left to right): 8, 64, 16, 300, 32
#fire rate fastest to slowest: Heavy Weapon, SMG, Assault Rifle, Pistol, Shotgun
#weapon damage highest to lowest: Shotgun, Assault Rifle, SMG, Pistol, Heavy Weapon

#WN
wn = trtl.Screen()
#Turtles
bullet = trtl.Turtle()
bullet.hideturtle()

#Variables
bullets = []
bulletNum = -1
BulletX = 0
BulletY = 0
BulletHeading = 0
Lruns = 0


#This function sets the bullet 
def generateBullet(X,Y,HEADING):
    global bulletNum

    #Makes bullet
    bulletNum = bulletNum + 1
    bullet = trtl.Turtle()
    bullet.penup()
    bullets.append(bullet)

    #Sets bullet
    bullets[bulletNum].setx(X)
    bullets[bulletNum].sety(Y)
    bullets[bulletNum].setheading(HEADING)
    wn.update()


def moveBullet():
    wn.update()
    global bulletNum
    global BulletX
    global BulletY
    global BulletHeading
    global Lruns


    for activeBullet in bullets:
        Lruns = Lruns + 1
        #Reports bullet current position to be handled by main.py
        if Lruns % 100 == 0:
            BulletX = activeBullet.xcor()
            BulletY = activeBullet.ycor()
            BulletHeading = activeBullet.heading()
        
        #Maybe make this a variable?
        activeBullet.forward(.2)

        #This removes the bullet when it goes out of bounds/hits a wall
        if activeBullet.xcor() > 300 or activeBullet.xcor() < -300 or activeBullet.ycor() > 300 or activeBullet.ycor() < -300:
            activeBullet.hideturtle()
            bullets.remove(activeBullet)
            bulletNum = bulletNum - 1



        