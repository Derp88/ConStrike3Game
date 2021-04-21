import turtle as trtl
import gun
import time

runs = 0
def aiMove(enemy,playerX,playerY):
    global runs
    runs = runs + 1
    enemy.setheading(enemy.towards(playerX,playerY))
    enemy.speed(1)
    enemy.forward(.025)
    #Maybe find a better way then modulus? A time based system is preferable
    if runs % 500 == 0:
        gun.generateBullet(enemy.xcor(),enemy.ycor(),enemy.heading())