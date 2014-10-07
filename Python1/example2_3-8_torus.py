#3,8 Torus knot
import rhinoscriptsyntax as rs
import math


points = [] #declares the size of my point array

pi = math.pi

#rs.EnableRedraw(False)

for t in rs.frange(0,360,1):

    rads = t*pi/2 #defines the rotation angle which is equal to time t multiplied by angular velocity

#mathematical description of a 3,8 Torus knot
    x = (3+ 2*math.cos(rads))*math.cos(t)
    y = (3+2*math.cos(rads))*math.sin(t)
    z = 2*math.sin(rads)

    n = rs.AddPoint([x, y, z])
    points.append(n)

rs.AddInterpCurve(points)

#rs.EnableRedraw(True)
