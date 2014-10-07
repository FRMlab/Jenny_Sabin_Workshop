import rhinoscriptsyntax as rs
import math

#3-8 torus knot
rs.EnableRedraw(False)
# define global variables
points = [] #declares size of my point array
pi = math.pi

    
def fib(n):  #return Fibonacci series up to value of n
#Return a list containing the Fibonacci series up to n
    result = []
    a,b = 0,1   #define a=0 & b=1
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result
    result.append(n)
r = fib(200)  #calling the function
   
for t in rs.frange(0, 360, 1):
    
    rads = t*pi/2 #defines the rotation angle which is equal to time t multiplied by angular velocity

    #mathematical description of a 3-8 torus knot

    x = (3+2*math.cos(rads*1/r[4]))*math.cos(t)
    y = (3+2*math.cos(rads))*math.sin(t)
    z = 2*math.sin(rads)
    
    n = rs.AddPoint([x,y,z])
    
    points.append(n)

rs.AddInterpCurve(points)
rs.EnableRedraw(True)







