import math
import rhinoscriptsyntax as rs

pi = math.pi
dblTwistAngle = 0.0

rs.EnableRedraw(False)

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

for z in rs.frange(0,5,1):
    dblTwistAngle = dblTwistAngle + (pi/30)

    for a in rs.frange(0.0, 2*pi, (pi/15)):
        x = 5*math.sin(a+dblTwistAngle)
        y = 5*math.cos(a+dblTwistAngle)
        rs.AddSphere([x,y,z],r[z])
        
        rs.EnableRedraw(True)