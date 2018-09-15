import turtle


import math

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n 
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, angle = 360)

beltran = turtle.Turtle()
beltran.pen (pensize = "3")
r = 100
r2 = r/2
r3 = r/6

arc (beltran, r2 , angle = 180)
arc (beltran, r , angle = 180)
beltran.penup()
arc (beltran, r2 , angle = 180)
beltran.pendown()
arc (beltran, r2 , angle = 180)

arc (beltran, r, angle = 180)
beltran.fd(r3)
beltran.penup()
beltran.lt(90)
beltran.fd (r2)
beltran.pendown()


circle (beltran, r3)

beltran.penup()
beltran.fd(r)
beltran.pendown()

circle (beltran, r3)

turtle.mainloop()