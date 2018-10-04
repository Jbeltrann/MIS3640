import math

def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a 
        x1 = (-b-math.sqrt(b**2-4*a*c))/2*a
        print("X equals:", x, " and", x1) 
    else:
        print("Does not have an answer")    
quadratic(5,9,-11)