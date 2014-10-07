import rhinoscriptsyntax as rs
import math
#3-8 torus knot

points = [] #declares the size of my point array
pi = math.pi

rs.EnableRedraw(False)
for t in rs.frange(0,90,1):
    
    def fib(n): #return Fibonacci series up to the value of N
       #return a list containing the fibonacci series to n
       result=[]
       a,b = 0,1
       while a < n:
           result.append(a)
           a,b = b,a+b
       return result
       result.append(n)
       
    r = fib(20000000000000000000000000000000000000000000000000000000000) #calling the function
    
    
    rads = r[t]*pi/2 #defines the rotation angle which is equal to time t multiplied by angular velocity
    
    
    #mathematical description of a 3-8 torus knot
    
    x=(3+2*math.cos(rads))*math.cos(r[t])
    y=(3+2*math.cos(rads))*math.sin(r[t])
    z=2*math.sin(rads)
    
    n=rs.AddPoint([x,y,z])
    points.append(n)
    
rs.AddInterpCurve(points)
rs.EnableRedraw(True)
