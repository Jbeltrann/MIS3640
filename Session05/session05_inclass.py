import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
   angle = 360 / n
   polyline(t, n, length, angle)

def circle(t,r):
    circumference =  2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, length, n)

def arc(t, r, angle):
    arc_length= 2 * math.pi * r * angle / 360
    n = int(arc_length /3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)
    
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

beltran = turtle.Turtle()

def circle (t, r):
    arc(t, r, angle = 360)

circle(beltran, r = 100)
beltran.lt(angle = 60)

for i in range(3):
    arc(beltran, r= 100, angle= 120)
    beltran.lt(angle = 120)


beltran.rt(angle = 60)
arc(beltran, r= 100, angle = 60)
beltran.lt(angle = 60)

for i in range(3):
    arc(beltran, r = 100, angle = 120)
    beltran.lt(angle = 120)

turtle.mainloop()


# square(beltran, 200)
# polygon(beltran, 100, 10)
# circle(beltran, 150)
# polygon(t=beltran, n = 7, length = 70)
# arc(beltran, 50, 75)
# polyline(beltran, 3, 100, 30)
