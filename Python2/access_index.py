#3,8 Torus knot
import rhinoscriptsyntax as rs
import math


points = [] #declares the size of my point array

pi = math.pi

#rs.EnableRedraw(False)


def fib(n): #return fibonacci series up to n
#return a list containing the fibonacci series up to n
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result
    result.append(n)
    
r = fib(100) #call it

z=0
for z in rs.frange(0,5,1):

    for t in rs.frange(0,360,1):

        rads = t*pi/2 #defines the rotation angle which is equal to time t multiplied by angular velocity

#mathematical description of a 3,8 Torus knot
        x = (3+ 2*math.cos(rads))*math.cos(t)
        y = (3+2*math.cos(rads))*math.sin(t)
    
        n = rs.AddPoint([x, y, r[z]])
        points.append(n)

rs.AddInterpCurve(points)

#rs.EnableRedraw(True)
